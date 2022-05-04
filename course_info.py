import pandas as pd


def _in_title(course_title: str, df):
    """Check if the course title is in the given dataframe"""
    return course_title in list(df["title"])


def _in_number(course_number: str, df):
    """Check if the course number is in the given dataframe"""
    return course_number in list(df["course_number"])


def course_importance(course_number: str=None, course_title: str=None) -> None:
    """Use this function to figure out if one specific course is important for getting enough core or
       courselist courses. It should also check if the course is a general competence, technological specialization
       or elective course.
       Input:
            Either a course number of a course name should be input.
        Output:
            No output, but the function prints important info for the studyplan."""
    assert not (course_number is None and course_title is None), "At least course title or number should be given."
    has_run = False
    if course_number is not None:
        if course_title is not None:
            print(f"\nAnalyzing {course_number} {course_title}...")
            print("-------------------------------------------------------")
        else:
            print(f"\nAnalyzing {course_number}...")
            print("------------------")
        is_course = _in_number(course_number, courselist)
        is_core = _in_number(course_number, core)
        is_general = _in_number(course_number, general_1) or _in_number(course_number, general_2)
        is_techno = _in_number(course_number, techno)
        if is_course:
            print("The course is on courselist.")
        if is_core:
            print("The course is on core.")
        if is_general:
            print("The course is General Competence.")
        elif is_techno:
            print("The course is Technological Specialization.")
        else:
            print("The course is an Elective")
        has_run = True

    if course_title is not None and not has_run:
        print(f"\nAnalyzing {course_title}...")
        print("-" * (13 + len(course_title)))
        is_course = _in_title(course_title, courselist)
        is_core = _in_title(course_title, core)
        is_general = _in_title(course_title, general_1) or _in_title(course_title, general_2)
        is_techno = _in_title(course_title, techno)
        if is_course:
            print("The course is on courselist.")
        if is_core:
            print("The course is on core.")
        if is_general:
            print("The course is General Competence.")
        elif is_techno:
            print("The course is Technological Specialization.")
        else:
            print("The course is an Elective")



if __name__ == '__main__':
    current_courses = pd.read_csv("current_courses.csv", sep='\t', dtype={0: str, 1: str, 2: str, 3: float})

    # Load courses for certificate
    core = pd.read_csv("data_science_requirements/core.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})
    courselist = pd.read_csv("data_science_requirements/courselist.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})

    # Load courses for categories
    general_1 = pd.read_csv("master_requirements/general_competence_1.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})
    general_2 = pd.read_csv("master_requirements/general_competence_2.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})
    techno = pd.read_csv("master_requirements/technological_specialization.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})

    # Which course will be taken
    course_number = "02807"
    course_title = "Computational Tools for Data Science"

    course_importance(course_number=None, course_title=course_title)
