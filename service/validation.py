import re
from espn_api.basketball import League
from espn_api.requests.espn_requests import ESPNInvalidLeague, ESPNAccessDenied, ESPNUnknownError


def is_valid_input_str(input_str):

    valid_numbers = re.findall(r'\d', input_str)
    if valid_numbers:
        return ''.join(valid_numbers)
    else:
        return ''


def print_data_from_inputs(inputid, inputyr):
    if len(inputid) == 10:
        if len(inputyr) == 4:
            try:
                league = League(league_id=int(inputid), year=int(inputyr))
                team0name = re.search(r'\((.*?)\)', str(league.teams[0])).group(1)
                return f"{team0name}"
            except ESPNAccessDenied:
                return "It seems that access to viewing this league is limited"
            except ESPNInvalidLeague:
                return "I can't find a league with that ID for this year\nPlease check your data and try again"
            except ESPNUnknownError:
                return f"Something went wrong\nPlease contact me https://t.me/lowbylow"
        else:
            return "Please enter correct year"
    else:
        return "Please enter correct league ID"
