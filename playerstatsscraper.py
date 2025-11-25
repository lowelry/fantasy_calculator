"""Получение статистики игрока NBA по имени и сезону."""

import json
from collections import OrderedDict
from pathlib import Path
from typing import Dict, List

from nba_api.stats.endpoints import PlayerGameLog
from nba_api.stats.static import players


PLAYER_NAME = "Stephen Curry"  # Имя игрока как в базе nba_api
SEASON = "2025-26"
SEASON_TYPE = "Regular Season"
SEASON_COUNT = 5  # текущий сезон + четыре предыдущих

# Ненужные столбцы, которые удаляем перед сохранением
UNUSED_COLUMNS = {
    "WL",
    "MIN",
    "FGA",
    "FG_PCT",
    "FG3A",
    "FG3_PCT",
    "FTM",
    "FTA",
    "FT_PCT",
    "OREB",
    "DREB",
    "TOV",
    "PF",
    "PLUS_MINUS",
    "VIDEO_AVAILABLE",
}


def find_player_id(full_name: str) -> int:
    """Возвращает ID игрока по полному имени."""

    matches = players.find_players_by_full_name(full_name)
    if not matches:
        raise ValueError(f"Игрок с именем '{full_name}' не найден")

    # Сначала ищем активного игрока, если таких нет — берём первое совпадение
    for candidate in matches:
        if candidate.get("is_active"):
            return candidate["id"]

    return matches[0]["id"]


def build_output_path(player: str) -> Path:
    """Формирует имя JSON-файла для агрегированных сезонов."""

    safe_name = player.lower().replace(" ", "_")
    return Path(f"{safe_name}_multi_seasons.json")


def fetch_player_stats_for_season(
    player_id: int, season: str, season_type: str
):
    """Возвращает DataFrame со статистикой за сезон или None, если игр нет."""

    game_log = PlayerGameLog(
        player_id=player_id,
        season=season,
        season_type_all_star=season_type,
    )

    df = game_log.get_data_frames()[0]
    df_filtered = df.drop(columns=list(UNUSED_COLUMNS), errors="ignore")

    if df_filtered.empty:
        return None

    df_filtered["FPTS"] = (
        df_filtered["FGM"] * 0.2
        + df_filtered["FG3M"] * 0.3
        + df_filtered["REB"] * 0.1
        + df_filtered["AST"] * 0.2
        + df_filtered["STL"] * 0.4
        + df_filtered["BLK"] * 0.4
        + df_filtered["PTS"] * 0.1
    ).round(2)

    return df_filtered


def season_sequence(latest_season: str, count: int) -> List[str]:
    """Формирует список сезонов начиная с последнего и количество count."""

    seasons = []
    current_start = int(latest_season.split("-")[0])
    for _ in range(count):
        next_end = (current_start + 1) % 100
        seasons.append(f"{current_start}-{next_end:02d}")
        current_start -= 1
    return seasons


def process_season(player_name: str, player_id: int, season: str, season_type: str) -> Dict:
    """Обрабатывает один сезон, возвращая словарь данных и флаг not_draft_yet."""

    df_filtered = fetch_player_stats_for_season(player_id, season, season_type)

    season_payload: Dict[str, object] = {"not_draft_yet": df_filtered is None}

    if df_filtered is None:
        print(
            f"Для игрока '{player_name}' нет игр в сезоне {season} ({season_type})."
            " Устанавливаем not_draft_yet=true."
        )
        return season_payload

    games_count = len(df_filtered)
    fpts_pstd = df_filtered["FPTS"].std(ddof=0)
    fpts_vstd = df_filtered["FPTS"].std(ddof=1)

    print(df_filtered.head())
    print(
        f"Популяционная стабильность {player_name}: {fpts_pstd:.2f}"
        f" на основе {games_count} игр в сезоне {season}"
    )
    print(
        f"Выборочная стабильность {player_name}: {fpts_vstd:.2f}"
        f" на основе {games_count} игр в сезоне {season}"
    )

    season_payload.update(
        {
            "not_draft_yet": False,
            "games_count": games_count,
            "fpts_pop_std": round(fpts_pstd, 2) if fpts_pstd == fpts_pstd else None,
            "fpts_sample_std": round(fpts_vstd, 2) if fpts_vstd == fpts_vstd else None,
            "matches": df_filtered.to_dict(orient="records"),
        }
    )

    return season_payload


def main() -> None:
    try:
        player_id = find_player_id(PLAYER_NAME)
        seasons = season_sequence(SEASON, SEASON_COUNT)

        aggregated_data: Dict[str, Dict] = OrderedDict()

        for season in seasons:
            aggregated_data[season] = process_season(
                PLAYER_NAME, player_id, season, SEASON_TYPE
            )

        output_path = build_output_path(PLAYER_NAME)
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(aggregated_data, f, ensure_ascii=False, indent=2)

        print(f"Все данные сохранены в файл {output_path}")
    except ValueError as exc:
        print(f"Ошибка: {exc}")
    except Exception as exc:
        print(f"Неожиданная ошибка: {exc}")


if __name__ == "__main__":
    main()