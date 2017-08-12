function remove_element(id) {
    element=document.getElementById(id);
    if (element==null){console.log('element doesn`t exsit');return null}
    element.parentNode.removeChild(element);
    element.destroy;
}

var app = angular.module("app",[]);
app.controller("ctrl", function($scope,$timeout) {
    $scope.h1 ='Joke`s on you Hater';
    $scope.fg='white';
    $scope.bg='black';
    $scope.remove_text='CLICK HERE TO DESTROY';
    if ($scope.fg=='whoisthebestprez?'){
        $scope.vid='<iframe width="854" height="480" src="https://www.youtube.com/embed/ek73ebks39w?ecver=1" frameborder="0" allowfullscreen></iframe>';}
    $scope.remove=function(){
    $scope.remove_text=0;// sorry, But a Blocking Wait() function would have taken more code, looked ugly and completely unnecessary
    $timeout(function(){$scope.remove_text+=1},1000)
    $timeout(function(){$scope.remove_text+=1},2000)
    $timeout(function(){$scope.remove_text+=1},3000)
    $timeout(function(){$scope.remove_text+=1},4000)
    $timeout(function(){$scope.remove_text+=1},5000)
    $timeout(function(){remove_element('amsgtoallhaters');$scope.remove_text='DONE'},5000)
    }
});
