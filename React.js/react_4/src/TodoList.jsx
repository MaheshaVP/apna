import { useState } from "react";
import { v4 as uuidv4 } from 'uuid';

export default function TodoList() {
    let [todos,setTodos] = useState([{task: "sample-task" , id: uuidv4(),isDone:false}]);
    let[newTodo,setNewTodo] = useState("");

    function addNewTask() {
        setTodos((prevTodos)=> {
            return[...prevTodos,{task:newTodo, id:uuidv4(),isDone:false}]
        });
        setNewTodo("");
    }

    let updateTodoValue= (event) => {
        setNewTodo(event.target.value);
    }

    let deleteTodo = (id) => {
        setTodos((prevTodos)=>todos.filter((prevTodos)=>prevTodos.id != id));
    }

    let markAllDone = () => {
        setTodos ( (prevTodos) => 
            prevTodos.map((todo)=> {
            return{
                ...todo,
                // task:todo.task.toUpperCase()
                isDone:true,
            };
        })
    );
    };

    let markasDone = (id) => {
        setTodos ( (prevTodos) => 
            prevTodos.map((todo)=> {
                if(todo.id == id) {
                    return{
                        ...todo,
                        isDone:true,
                    };
                }else{
                    return todo;
                }
            
        })
    );
    }

    let uppercaseAll = () => {
        setTodos((todos) => 
        todos.map((todo) => {
            return{
                ...todo,
                task:todo.task.toUpperCase(),
            };
        })
        );
    }

    return(
        <div>

            <input placeholder="add a task" 
            value={newTodo} 
            onChange={updateTodoValue}>
            </input>
            <br />
            <br />
            <button onClick={addNewTask}>Add Task</button>
            <br />
            <br />

            <hr />
            <h4>Tasks Todo</h4>
            <ul>
                {
                    todos.map((todo)=> (
                        <li key={todo.id}>
                            <span style={todo.isDone? {textDecorationLine:"line-through"} : {}}>
                                {todo.task}
                                </span>
                            &nbsp;&nbsp;&nbsp;
                            <button onClick={()=>deleteTodo(todo.id)}>delete</button> &nbsp;&nbsp;
                            <button onClick={()=>markasDone(todo.id)}>Mark As Done</button>
                            </li>
                    ))
                }
            </ul>
            <button onClick={uppercaseAll}>Uppercase All</button>
            <br />
            <button onClick={markAllDone}>Mark All as Done</button>
                
                

        </div>
    );
  }