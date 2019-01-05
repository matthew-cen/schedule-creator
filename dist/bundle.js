/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./js-src/main.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./js-src/main.js":
/*!************************!*\
  !*** ./js-src/main.js ***!
  \************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("(() => {\n\tdocument.addEventListener(\"DOMContentLoaded\", () => {\n\t\tconst addCourseForm = document.getElementById(\"addCourseForm\");\n\t\tconst courseList = document.getElementById(\"courseList\");\n\t\tconst addCourseModal = document.getElementById(\"createCourseModal\");\n\t\tconst addCourseBtn = document.getElementById(\"addCourseBtn\");\n\t\tconst addCourseModalCloseBtn = document.getElementById(\n\t\t\t\"addCourseCloseModal\",\n\t\t);\n\t\tconst addCourseCancelBtn = document.getElementById(\n\t\t\t\"addCourseCancelBtn\",\n\t\t);\n\n\t\t// UTILITY FUNCTIONS\n\t\tfunction toggleAddCourseModal() {\n\t\t\taddCourseModal.classList.toggle(\"is-active\");\n\t\t}\n\n\t\t// Event Listeners\n\t\t// Add Course Modal Toggling\n\t\taddCourseBtn.addEventListener(\"click\", toggleAddCourseModal);\n\t\taddCourseModalCloseBtn.addEventListener(\"click\", toggleAddCourseModal);\n\t\taddCourseCancelBtn.addEventListener(\"click\", toggleAddCourseModal);\n\n\t\t// Form Submit Button\n\t\taddCourseForm.addEventListener(\"submit\", event => {\n\t\t\tevent.preventDefault(); // disable default page refresh behavior on submit\n\t\t\tconsole.log(\"Ran Add Course\");\n\t\t\tlet addCourseFormData = new FormData(addCourseForm); // create FormData from form element\n\t\t\taddCourse(...addCourseFormData.values());\n\t\t\t// fetch(\"/api/hello\")\n\t\t\t// \t.then(res => {\n\t\t\t// \t\tconsole.log(res);\n\t\t\t// \t})\n\t\t\t// \t.catch(err => {\n\t\t\t// \t\tconsole.error(\"An error occurred\");\n\t\t\t// \t});\n\t\t\ttoggleAddCourseModal(\n\t\t\t\t\n\t\t\t); // close modal\n\t\t});\n\n\t\t// add new course\n\t\tfunction addCourse(courseID, courseName) {\n\t\t\t// SEND DATA TO SERVER FOR VALIDATION\n\t\t\t// STORE COURSE DATA IN SESSIONSTORAGE\n\t\t\t// RENDER NEW COURSE COMPONENT\n\t\t\tconst newCourseComponent = `\n\t\t\t<div class=\"notification is-primary is-12 box\" courseID=\"${courseID}\">\n\t\t\t<button class=\"delete\"></button>\n\t\t\t<div class=\"columns\">\n\t\t\t<div class=\"column is-11\">\n\t\t\t<p class=\"title\">${courseID} - ${courseName}</p>\n\t\t\t</div>\n\t\t\t<div class=\"column is-1\">\n\t\t\t<button class=\"button is-white\">\n\t\t\t<span class=\"icon\">\n\t\t\t<i class=\"fas fa-pencil-alt fa-lg\"></i>\n\t\t\t</span>\n\t\t\t<span>\n\t\t\tEdit\n\t\t\t</span>\n\t\t\t</button>\n\t\t\t</div>\n\t\t\t</div>\n\t\t\t</div>`;\n\t\t\tcourseList.insertAdjacentHTML(\"beforeend\", newCourseComponent);\n\t\t}\n\t\t// remove existing course\n\t\tfunction removeCourse() {\n\t\t\t// SEND DATA TO SERVER FOR VALIDATION\n\t\t\t// REMOVE COURSE DATA IN SESSIONSTORAGE\n\t\t\t// NRENDER COURSE COMPONENT\n\t\t}\n\t\t// update course information\n\t\tfunction updateCourse() {\n\t\t\t// SEND DATA TO SERVER FOR VALIDATION\n\t\t\t// UPDATE COURSE DATA IN SESSIONSTORAGE\n\t\t\t// RERENDER COURSE COMPONENT\n\t\t}\n\n\t\t// retrieve course data from server and store it in browser\n\t\tfunction getCourse() {\n\t\t\t// SEND DATA TO SERVER FOR VALIDATION\n\t\t\t// STORE COURSE DATA IN SESSIONSTORAGE\n\t\t\t// RENDER NEW COURSE COMPONENT\n\t\t}\n\t});\n})();\n\n\n//# sourceURL=webpack:///./js-src/main.js?");

/***/ })

/******/ });