console.log("starting a task");
const user =getUsers(1, (user)=>{
    console.log("user", user)
});
console.log("ending a task");

function getUsers(id,callback){
    setTimeout(()=>{
        console.log("getting users from a database");
        callback({id:id, username:"simon kamau"});
    },2000)
}

function getMovies(id,callback){
    
}