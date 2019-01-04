function toggleModal() {
	document.querySelector(".modal").classList.toggle("is-active");
}
// FIXME: Fix onload behavior to trigger when the DOM tree or certain elements are loaded
// use DOMContentLoaded
document.addEventListener("DOMContentLoaded", () => {
	// Event Listeners
	// Custom AJAX handling for form submission
	let addCourseForm = document.querySelector("form");

	// Override Form Submit Behavior
	addCourseForm.addEventListener("submit", event => {
		event.preventDefault(); // disable default page refresh behavior on submit
		let addCourseFormData = new FormData(addCourseForm); // create FormData from form element
		fetch("/api/hello")
			.then(res => {
				console.log(res);
			})
			.catch(err => {
				console.error("An error occurred");
			});
	});
});

// add new course
function addCourse() {
	// SEND DATA TO SERVER FOR VALIDATION
	// STORE COURSE DATA IN SESSIONSTORAGE
	// RENDER NEW COURSE COMPONENT
}
// remove existing course
function removeCourse() {
	// SEND DATA TO SERVER FOR VALIDATION
	// REMOVE COURSE DATA IN SESSIONSTORAGE
	// NRENDER COURSE COMPONENT
}
// update course information
function updateCourse() {
	// SEND DATA TO SERVER FOR VALIDATION
	// UPDATE COURSE DATA IN SESSIONSTORAGE
	// RERENDER COURSE COMPONENT
}

// retrieve course data from server and store it in browser
function getCourse() {
	// SEND DATA TO SERVER FOR VALIDATION
	// STORE COURSE DATA IN SESSIONSTORAGE
	// RENDER NEW COURSE COMPONENT
}
