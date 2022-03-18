import React from "react";
import { useState } from "react";

export default function LoginComponent() {
    const [input, setInput] = useState({});
    const action = "/login";
    const method = "POST";
    const handleChange = e => {
        setInput({ ...input, [e.target.name]: e.target.value });
    };
    const handleSubmit = async(e) => {
        e.preventDefault();

        await fetch(action, {
            method: method,
            headers: {
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

// export default class LoginComponent extends Component {
//     constructor(props, context) {
//         super(props, context);
//         this.state = {
//             input: {}
//         };

//         this.onChange = this.onChange.bind(this);
//         this.onSubmit = this.onSubmit.bind(this);
//     }

//     onChange(e) {
//       let input = this.state.input;
//       input[e.target.name] = e.target.value;

//       this.setState({
//         input
//       });
//     }

//     onSubmit(e) {
//       e.preventDefault();

//       fetch('/login', {
//         method: 'POST',
//         headers: {
//           'Accept': 'application/json',
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({
//           email: this.state.input.email,
//           password: this.state.input.password,
//         })
//       }).then(res => {
//         if (res.status === 200) {
//           this.props.history.push('/');
//         }
//       }).catch(err => {
//         console.log(err);
//       });
//     }

//     render() {
//         return (
//               <form
//                   id='login-form'
//                   action={this.props.action}
//                   method={this.props.method}
//                   onSubmit={this.onSubmit}
//                 >
//                   <label>
//                       Email:
//                       <input type="email" name="email" onChange={this.onChange}></input>
//                   </label>
//                   <br/>
//                   <label>
//                       Password:
//                       <input type="password" name="password" onChange={this.onChange}></input>
//                   </label>
//                   <br/>
//                   <input type="submit" value="Login"></input>
//               </form>
//         );
//     }
// }