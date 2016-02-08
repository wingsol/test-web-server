angular.module('myApp', [])
.controller('appCtrl', function($scope) {

  $scope.myClick = function() {
    console.log('YEP!');
  }

});
