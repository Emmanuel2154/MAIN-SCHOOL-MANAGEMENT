const BASE_URL = 'http://localhost:8000/api/v1'
const fetchStudents = async () => {
   let data = await fetch(`${BASE_URL}/students`)
   let students = await data.json()
   return students
}



(async ()=> {
    const result = await fetchStudents()
    console.log(result);
}
) ()