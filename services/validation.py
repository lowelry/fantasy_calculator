import re
from espn_api.basketball import League
from espn_api.requests.espn_requests import ESPNInvalidLeague, ESPNAccessDenied, ESPNUnknownError
from utils.extras import positive_color


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
                validation_data = ["reviewing moments, recounting numbers", f"{positive_color}"]
                return validation_data
            except ESPNAccessDenied:
                validation_data = ["It seems that access to viewing this league is limited", f"{positive_color}"]
                return validation_data
            except ESPNInvalidLeague:
                validation_data = ["I can't find a league with that ID for this year\nPlease check your data and try "
                                   "again", f"{positive_color}"]
                return validation_data
            except ESPNUnknownError:
                validation_data = [f"Something went wrong\nPlease contact me https://t.me/lowbylow",
                                   f"{positive_color}"]
                return validation_data
        else:
            validation_data = ["Please enter correct year", "#E462A8"]
            return validation_data
    else:
        validation_data = ["Please enter correct league ID", "#E462A8"]
        return validation_data
