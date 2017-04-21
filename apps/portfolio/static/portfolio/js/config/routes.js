MyApp.config(function($routeProvider){

	$routeProvider

	.when('/', {
		templateUrl: './../views/splash.html',
		controller: 'usersController'
	})
	.when('/neighborhood', {
		templateUrl: './../views/neighborhood.html',
		controller: 'usersController'
	})
	.when('/capture', {
		templateUrl: './../views/capture.html',
		controller: 'usersController'
	})
	//
	.otherwise('/')
})
