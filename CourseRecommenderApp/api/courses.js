const localUrl = 'http://127.0.0.1:5000/get_top_courses';
import axios from 'axios';

export const getCourses = async (searchParams) => {
    console.log(searchParams)
    try {
        const response = await axios.post(localUrl, searchParams);
        return response.data;
    } catch (err) {
        console.log('error fetching courses: ', err.message);
        throw err;
    }
}