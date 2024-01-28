const localUrl = 'http://127.0.0.1:5000/get_top_courses';
import axios from 'axios';
import allCourses from '../data/courses.json'

export const getCourses = async (searchParams) => {
    if (Object.keys(searchParams).length > 0) {
        try {
            const response = await axios.post(localUrl, searchParams);
            return response.data;
        } catch (err) {
            console.log('error fetching courses: ', err.message);
            throw err;
        }
    } else {
        return allCourses;
    }
};