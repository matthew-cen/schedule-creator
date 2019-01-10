import * as hyperHTML from "hyperhtml";

// Course Component
export function courseComponent(courseID, courseName) {
	function deleteCourseComponent(event) {
		event.target.parentNode.remove();
	}
	return hyperHTML.wire()`
	<div class="notification is-primary is-12 box" data-course_id="${courseID}">
        <button class="delete" onclick=${deleteCourseComponent}></button>
        <div class="columns">
            <div class="column is-11">
                <p class="title">${courseID} - ${courseName}</p>
            </div>
            <div class="column is-1">
                <button class="button is-white">
                    <span class="icon">
                        <i class="fas fa-pencil-alt fa-lg"></i>
                    </span>
                    <span>
                        Edit
                    </span>
                </button>
            </div>
        </div>
    </div>`;
}
