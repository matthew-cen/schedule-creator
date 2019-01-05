(() => {
	document.addEventListener("DOMContentLoaded", () => {
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

		// Event Listeners
		// Add Course Modal Toggling
		addCourseBtn.addEventListener("click", toggleAddCourseModal);
		addCourseModalCloseBtn.addEventListener("click", toggleAddCourseModal);
		addCourseCancelBtn.addEventListener("click", toggleAddCourseModal);

		// Form Submit Button
		addCourseForm.addEventListener("submit", event => {
			event.preventDefault(); // disable default page refresh behavior on submit
			console.log("Ran Add Course");
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
			// STORE COURSE DATA IN SESSIONSTORAGE
			// RENDER NEW COURSE COMPONENT
			const newCourseComponent = `
			<div class="notification is-primary is-12 box" data-course_id="${courseID}">
				<button class="delete"></button>
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
			courseList.insertAdjacentHTML("beforeend", newCourseComponent);

			// Event Listener for Delete Button
			document.querySelector(`div .notification[data-course_id="${courseID}"`)
				.addEventListener("click", event => {
					event.target.parentNode.remove() // removes course component 
				})
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
