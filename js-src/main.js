(() => {
	document.addEventListener("DOMContentLoaded", () => {
		const addCourseForm = document.getElementById("addCourseForm");
		const courseList = document.getElementById("courseList");
		const createCourseModal = document.getElementById("createCourseModal");

		// UTILITY FUNCTIONS
		function toggleModal() {
			createCourseModal.classList.toggle("is-active");
		}

		// Event Listeners
		// Modal Toggling
		document
			.getElementById("addCourseBtn")
			.addEventListener("click", toggleModal);
		document
			.querySelector("#createCourseModal header button")
			.addEventListener("click", toggleModal);

		// Custom AJAX handling for form submission

		// Form Submit Button
		addCourseForm.addEventListener("submit", event => {
			event.preventDefault(); // disable default page refresh behavior on submit
			addCourse();
			let addCourseFormData = new FormData(addCourseForm); // create FormData from form element
			// fetch("/api/hello")
			// 	.then(res => {
			// 		console.log(res);
			// 	})
			// 	.catch(err => {
			// 		console.error("An error occurred");
			// 	});
		});

		// add new course
		function addCourse() {
			// SEND DATA TO SERVER FOR VALIDATION
			// STORE COURSE DATA IN SESSIONSTORAGE
			// RENDER NEW COURSE COMPONENT
			courseList.insertAdjacentHTML("beforeend");
			const newCourseComponent = `
			<div class="notification is-primary is-12 box">
			<button class="delete"></button>
			<div class="columns">
			<div class="column is-11">
			<p class="title">CS-UY 2134 - Object
			Oriented
			Programming</p>
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
