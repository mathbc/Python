var app = angular.module('toDo', []);

app.controller('toDoController', function($scope, $http) {
    
    // $scope.todoList = [{todoText: 'Finish this app', done: false}]; // Array de Todo

    $http.get('/todo/api/').then(function(response) {
        console.log(response.data);
        $scope.todoList = response.data;
    });

    $scope.saveData = function() {
        var data = {todo_text: $scope.todoInput, done: false}
        $http.put('/todo/api/', data);
    };

    $scope.todoAdd = function() {
        $scope.todoList.push({todo_text: $scope.todoInput, done: false}) // Adiciona o valor do formulário ao array de todo
        $scope.todoInput = ''; // Limpa o formulário
    };

    $scope.remove = function() {
        var oldList = $scope.todoList; // Recupera a lista antiga
        $scope.todoList = [];
        angular.forEach(oldList, function(x) {
            if(x.done) {
                $http.delete(`/todo/api/${x.id}`);
            } else {
                $scope.todoList.push(x);
            }
        });
    }
});