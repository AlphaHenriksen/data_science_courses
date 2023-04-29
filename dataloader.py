import pandas as pd


def get_data(course_file):
    """Load the data for core, courselist, course type and the current courses."""
    current_courses = pd.read_csv(
        course_file, sep="\t", dtype={0: str, 1: str, 2: str, 3: float}
    )
    
    bachelor_courses = pd.read_csv(
        "bachelor_courses.csv", sep="\t", dtype={0: str, 1: str, 2: str, 3: float}
    )

    # Load courses for certificate
    core = pd.read_csv(
        "data_science_requirements/core.csv",
        sep="\t",
        dtype={0: str, 1: str, 2: float, 3: str},
    )
    courselist = pd.read_csv(
        "data_science_requirements/courselist.csv",
        sep="\t",
        dtype={0: str, 1: str, 2: float, 3: str},
    )

    # Load courses for categories
    general_1 = pd.read_csv(
        "master_requirements/general_competence_1.csv",
        sep="\t",
        dtype={0: str, 1: str, 2: float, 3: str},
    )
    general_2 = pd.read_csv(
        "master_requirements/general_competence_2.csv",
        sep="\t",
        dtype={0: str, 1: str, 2: float, 3: str},
    )
    techno = pd.read_csv(
        "master_requirements/technological_specialization.csv",
        sep="\t",
        dtype={0: str, 1: str, 2: float, 3: str},
    )
    return current_courses, bachelor_courses, core, courselist, general_1, general_2, techno
