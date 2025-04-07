from app.errors import OutdatedVaccineError, NotVaccinatedError, \
    NotWearingMaskError
from app.cafe import Cafe

def go_to_cafe(friends: list, cafe: Cafe):
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cofe(friend)
        except OutdatedVaccineError:
            print("All friends should be vaccinated")
        except NotVaccinatedError:
            print("All friends should be vaccinated")
        except NotWearingMaskError:
            print("Friends should buy {masks_to_buy} masks")
            masks_to_buy += 1
    if masks_to_buy != 0:
        print(f"Friends should buy {masks_to_buy} masks")
    return f"Friends can go to {cafe.name}"
