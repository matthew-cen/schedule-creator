const path = require("path");

module.exports = {
	entry: "./js-src/main.js",
	output: {
		path: path.resolve(__dirname, "dist"),
		filename: "bundle.js",
	},
	module: {
		rules: [
			{
				parser: {
					amd: false,
				},
			},
		],
	},
};
