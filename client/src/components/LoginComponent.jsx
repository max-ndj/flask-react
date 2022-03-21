import React from "react";
import { useState } from "react";

export default function LoginComponent() {
    const [input, setInput] = useState({});
    const action = "http://localhost:5000/login";
    const method = "POST";
    const handleChange = e => {
        setInput({ ...input, [e.target.name]: e.target.value });
    };
    const handleSubmit = async(e) => {
        e.preventDefault();

        await fetch(action, {
            method: method,
            headers: {
                "Access-Control-Allow-Origin": "*",
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: input.email,
                password: input.password
            })
        }).then(res => {
            console.log(res);
        }).catch(err => {
            console.log(err);
        });
    };

    return (
        <form
            id='login-form'
            action={action}
            method={method}
            onSubmit={handleSubmit}
        >
            <label>
                Email:
                <input type="email" name="email" onChange={handleChange}></input>
            </label>
            <br/>
            <label>
                Password:
                <input type="password" name="password" onChange={handleChange}></input>
            </label>
            <br/>
            <input type="submit" value="Login"></input>
        </form>
    );
}