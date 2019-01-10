import * as hyperHTML from "hyperhtml";
import * as components from "./components";

(() => {
	// Session Storage Initialization
	window.sessionStorage.setItem("courses", {});
	window.sessionStorage.setItem("loggedIn", false);

	document.addEventListener("DOMContentLoaded", () => {
		// PSUEDO GLOBALS
		let courses = {};
		const courseCounter = document.getElementById("courseCounter");
		const addCourseForm = document.getElementById("addCourseForm");
		const courseList = document.getElementById("courseList");
		const addCourseModal = document.getElementById("createCourseModal");
		const addCourseBtn = document.getElementById("addCourseBtn");
		const addCourseModalCloseBtn = document.getElementById(
			"addCourseCloseModal",
		);
		const addCourseCancelBtn = document.getElementById(
			"addCourseCancelBtn",
		);

		// UTILITY FUNCTIONS
		function toggleAddCourseModal() {
			addCourseModal.classList.toggle("is-active");
		}
		// RENDER FUNCTIONS
		function renderCourses() {
			hyperHTML.bind(courseList)`
				${Object.keys(courses).map(key =>
					components.courseComponent(key, courses[key]),
				)}
			`;
		}
		// Event Listeners
		// Add Course Modal Toggling
		addCourseBtn.onclick = toggleAddCourseModal;
		addCourseModalCloseBtn.onclick = toggleAddCourseModal;
		addCourseCancelBtn.onclick = toggleAddCourseModal;

		// Form Submit Button
		addCourseForm.addEventListener("submit", event => {
			event.preventDefault(); // disable default page refresh behavior on submit
			let addCourseFormData = new FormData(addCourseForm); // create FormData from form element
			// fetch("/api/hello")
			// 	.then(res => {
			// 		console.log(res);
			// 	})
			// 	.catch(err => {
			// 		console.error("An error occurred");
			// 	});
			addCourse(...addCourseFormData.values());
			toggleAddCourseModal();
		});

		// add new course
		function addCourse(courseID, courseName) {
			// SEND DATA TO SERVER FOR VALIDATION
			// STORE COURSE DATA
			courses[courseID] = {
				name: courseName,
			};
			// // RENDER NEW COURSE COMPONENT
			// courseList.insertAdjacentHTML("beforeend", newCourseComponent);
			renderCourses();

			// Increment course counter
			courseCounter.innerText = parseInt(courseCounter.innerText) + 1;
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
	});
})();
