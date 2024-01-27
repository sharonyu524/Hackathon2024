
'use client'


const Categories = ({ value, setValue }) => {

    return (
        <>
            <select
                className="chosen-single form-select"
                value={value}
                onChange={(e) => setValue(e.target.value)}
            >
                <option value="" disabled>What I value the most</option>
                <option defaultValue="44">Workload (Low)</option>
                <option defaultValue="106">Workload (high)</option>
                <option defaultValue="46">Difficulty (Low)</option>
                <option defaultValue="48">Difficulty (High)</option>
                <option defaultValue="47">Instructor Quality</option>
                <option defaultValue="45">Course Quality</option>
            </select>
            <span className="icon flaticon-star"></span>
        </>
    );
};

export default Categories;
