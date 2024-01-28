const localUrl = 'http://127.0.0.1:5000/get_top_courses';
import axios from 'axios';

export const getCourses = async (searchParams) => {
    console.log(searchParams)
    try {
        const response = await axios.post(localUrl, searchParams);
        return response.data;
    } catch (err) {
        console.log('error fetching courses: ', err.message);
        if (err.response) {
            // The server responded with a status code outside the 2xx range
            console.log('Response Data:', err.response.data);
            console.log('Response Status:', err.response.status);
            console.log('Response Headers:', err.response.headers);
        } else if (err.request) {
            // The request was made, but no response was received
            console.log('Request:', err.request);
        } else {
            // Something else caused the error
            console.log('Error Config:', err.config);
        }
        throw err;
    }
}