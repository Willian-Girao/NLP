'use strict'

//Prints the distance matrix.
function calculateDistance(distMatrix, wa, wb) {
	for (var i = 2; i < (wb.length + 2); i++) {
		for (var j = 2; j < (wa.length + 2); j++) {
			let collumnIndex = j;
			let lineIndex = i;

			while(distMatrix[0][collumnIndex] == distMatrix[lineIndex][0] && collumnIndex > 0 && lineIndex > 0) {
				collumnIndex--;
				if (i > 2) {
					lineIndex--;
				}
			}

			let deleteCost = parseInt(distMatrix[lineIndex][(collumnIndex - 1)]);
			let replaceCost = parseInt(distMatrix[(lineIndex - 1)][(collumnIndex - 1)]);
			let insertCost = parseInt(distMatrix[(lineIndex - 1)][collumnIndex]);

			let helper = deleteCost < replaceCost ? deleteCost : replaceCost;
			let smallestCost =  insertCost < helper ? insertCost : helper;

			distMatrix[i][j] = (smallestCost + 1).toString();
		}
	}

	return;
}

//Prints the distance matrix.
function printDistMatrix(distMatrix, wa, wb) {
	process.stdout.write('\n');
	for (var i = 0; i < (wb.length + 2); i++) {
		for (var j = 0; j < (wa.length + 2); j++) {
			process.stdout.write(distMatrix[i][j]);
			process.stdout.write(" ");
		}
		process.stdout.write('\n');
	}
	process.stdout.write('\n');

	return;
}

//Initializes the matriz utilized to calculate the Levenshtein Distance between two words.
function findLevenshteinDistance(word_a, word_b) {
	let distMatrix = [];

	for (var i = 0; i < (word_b.length + 2); i++) {
		distMatrix[i] = [];

		for (var j = 0; j < (word_a.length + 2); j++) {
			distMatrix[i][j] = '0';
		}	
	}

	distMatrix[0][0] = '-'; //free.
	distMatrix[0][1] = ' '; //setting empty word.
	distMatrix[1][0] = ' '; //setting empty word.

	let wa = word_a.split('');
	let wb = word_b.split('');

	//consuming word_a.
	for (var j = 2; j < (wa.length + 2); j++) {
		distMatrix[0][j] = wa[(j - 2)];
		distMatrix[1][j] = (j - 1).toString();
	}

	//consuming word_b.
	for (var i = 2; i < (wb.length + 2); i++) {
		distMatrix[i][0] = wb[(i - 2)];
		distMatrix[i][1] = (i - 1).toString();
	}

	//Calculating edit distances.
	for (var i = 2; i < (wb.length + 2); i++) {
		for (var j = 2; j < (wa.length + 2); j++) {
			let collumnIndex = j;
			let lineIndex = i;

			while(distMatrix[0][collumnIndex] == distMatrix[lineIndex][0] && collumnIndex > 2 && lineIndex > 2) {
				lineIndex--;
				collumnIndex--;
			}

			// console.log("lineIndex: ", lineIndex);
			// console.log("collumnIndex: ", collumnIndex);

			if (collumnIndex > 2 || lineIndex > 2) {
				let deleteCost = parseInt(distMatrix[lineIndex][(collumnIndex - 1)]);
				let replaceCost = parseInt(distMatrix[(lineIndex - 1)][(collumnIndex - 1)]);
				let insertCost = parseInt(distMatrix[(lineIndex - 1)][collumnIndex]);

				let helper = deleteCost < replaceCost ? deleteCost : replaceCost;
				let smallestCost =  insertCost < helper ? insertCost : helper;

				distMatrix[i][j] = (smallestCost + 1).toString();
			} else {
				distMatrix[i][j] = '0';
			}
		}
	}

	let dif = (parseInt(distMatrix[word_b.length + 1][word_a.length + 1]) * 100) / word_b.length;

	console.log('\n_________________________________');
	console.log("\nWord A: ", word_a);
	console.log("Word B: ", word_b);
	console.log("\nLevenshtein distance: ", distMatrix[word_b.length + 1][word_a.length + 1]);
	console.log("Structural difference: ", dif);
	console.log('_________________________________');

	return parseInt(distMatrix[word_b.length + 1][word_a.length + 1]);
}

//Initializes the matriz utilized to calculate the Levenshtein Distance between two words.
function findStructuralDifference(word_a, word_b) {
	let distMatrix = [];

	for (var i = 0; i < (word_b.length + 2); i++) {
		distMatrix[i] = [];

		for (var j = 0; j < (word_a.length + 2); j++) {
			distMatrix[i][j] = '0';
		}	
	}

	distMatrix[0][0] = '-'; //free.
	distMatrix[0][1] = ' '; //setting empty word.
	distMatrix[1][0] = ' '; //setting empty word.

	let wa = word_a.split('');
	let wb = word_b.split('');

	//consuming word_a.
	for (var j = 2; j < (wa.length + 2); j++) {
		distMatrix[0][j] = wa[(j - 2)];
		distMatrix[1][j] = (j - 1).toString();
	}

	//consuming word_b.
	for (var i = 2; i < (wb.length + 2); i++) {
		distMatrix[i][0] = wb[(i - 2)];
		distMatrix[i][1] = (i - 1).toString();
	}

	//Calculating edit distances.
	for (var i = 2; i < (wb.length + 2); i++) {
		for (var j = 2; j < (wa.length + 2); j++) {
			let collumnIndex = j;
			let lineIndex = i;

			while(distMatrix[0][collumnIndex] == distMatrix[lineIndex][0] && collumnIndex > 2 && lineIndex > 2) {
				lineIndex--;
				collumnIndex--;
			}

			// console.log("lineIndex: ", lineIndex);
			// console.log("collumnIndex: ", collumnIndex);

			if (collumnIndex > 2 || lineIndex > 2) {
				let deleteCost = parseInt(distMatrix[lineIndex][(collumnIndex - 1)]);
				let replaceCost = parseInt(distMatrix[(lineIndex - 1)][(collumnIndex - 1)]);
				let insertCost = parseInt(distMatrix[(lineIndex - 1)][collumnIndex]);

				let helper = deleteCost < replaceCost ? deleteCost : replaceCost;
				let smallestCost =  insertCost < helper ? insertCost : helper;

				distMatrix[i][j] = (smallestCost + 1).toString();
			} else {
				distMatrix[i][j] = '0';
			}
		}
	}

	let dif = (parseInt(distMatrix[word_b.length + 1][word_a.length + 1]) * 100) / word_b.length;

	console.log('\n_________________________________');
	console.log("\nWord A: ", word_a);
	console.log("Word B: ", word_b);
	console.log("\nStructural difference: ", dif);
	console.log('_________________________________');

	return diff;
}

function levenshteinDist(word_a, word_b) {
	//matrix holding the actions values.

	//let editDistance = findLevenshteinDistance(word_a, word_b);
	let structuralDiff = findStructuralDifference(word_a, word_b);

	return;
}

// levenshteinDist("benyam", "ephrem");
levenshteinDist(process.argv[2].toString(), process.argv[3].toString());