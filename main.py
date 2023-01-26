from master_requirements.master_courses import ects_requirements
from data_science_requirements.data_science_courses import (
    ects_above_required,
    alternative_courses,
)
from course_info import course_importance
from dataloader import get_data

if __name__ == "__main__":
    current_courses, core, courselist, general_1, general_2, techno = get_data(
        "current_courses_jan23.csv"
    )

    # How are the courses seperated into general, technological, elective, master
    ects_requirements(current_courses, general_1, general_2, techno)

    # Show core and courselist
    ects_above_required(current_courses, core, courselist)

    # Show which other core and courselist courses could be taken
    # alternative_courses(current_courses, core, courselist)

    # Show where one course is included
    course_importance(
        current_courses,
        core,
        courselist,
        general_1,
        general_2,
        techno,
        course_number=None,
        course_title="Advanced Image Analysis",
    )
