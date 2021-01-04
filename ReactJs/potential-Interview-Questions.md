## React Js Potential Interview Questions

#### What are the features of React?

- JSX: JSX is a syntax extension to JavaScript. It is used with React to describe what the user interface should look like. By using JSX, we can write HTML structures in the same file that contains JavaScript code.
- Components: Components are the building blocks of any React application, and a single app usually consists of multiple components. It splits the user interface into independent, reusable parts that can be processed separately.
- Virtual DOM: React keeps a lightweight representation of the real DOM in the memory, and that is known as the virtual DOM. When the state of an object changes, virtual DOM changes only that object in the real DOM, rather than updating all the objects.
- One-way data-binding: React’s one-way data binding keeps everything modular and fast. A unidirectional data flow means that when designing a React app, you often nest child components within parent components.
- High performance: React updates only those components that have changed, rather than updating all the components at once. This results in much faster web applications.

#### Hello World

- Speciality in react library
- Features of react than others
- What is a arrow function , why we use a arrow function
- Difference between react and angular
- Data binding, mvc , speed , serverside and client side

#### Introducing JSX

- What is JSX?
- Regular javascript translators for browsers (eg: babel) / (transpiler)

#### Rendering Elements

- Dom vs virtual dom
- Why virtual dom is important in rendering

#### Components and Props

- Stateful and stateless component in class components
- Difference between props and states
- How to pass props in react
- Proptypes
- What is a higher-order component in React?
- Prop drilling
- React context api

#### State and Lifecycle

- How to pass a function to a child component?
- How components are refreshed ( life cycle )
- How to handle componentDidUpdate without infinite loop
- How are class components rendered? Please explain step wise
- What are the different phases of react lifecycle
- Implementation of state ( with constructor and without )
- Update a state ( asynchronous )
- how to handle a event that should hapen after state update
- Why we don't update by directly assigning a value
- What are the two methods to update state
- React Fragments
- Life cycle - mount unmount update / handling in class and hooks
- Hooks? Use Effect usage render every time , render only on intial loading , render on change of state variable
- useMemo - usage
- useEffect - order matters / how to handle async / mounting / update / unmoumt states in useEffect

#### Handling Events

- What is an event in React?
- What are synthetic events in React?
- What is the use of this keyword?

#### Conditional Rendering

- Implement a code for conditional rendering
- Difference between conditional rendering and component hidden

#### Lists and Keys

- Explain how lists work in React
- Important of Keys
- What is the need of using keys in a list
- Is it okay to use index as a key?
- Why other component does not have key attribute?

#### Lifting State Up

- What do you mean by state uplifting?
- How can we omit props drilling?

#### Redux and components of redux

- Redux's intent can be summarized in three principles
  - Global app state is kept in a single store
  - The store state is read-only to the rest of the app
  - Reducer functions are used to update the state in response to actions
- Redux uses a "one-way data flow" app structure
  - State describes the condition of the app at a point in time, and UI renders based on that state
  - When something happens in the app:
  - The UI dispatches an action
  - The store runs the reducers, and the state is updated based on what occurred
  - The store notifies the UI that the state has changed
  - The UI re-renders based on the new state
- use case of Redux thunk
  - One of the main use cases for this middleware is for handling actions that might not be synchronous, for example, using axios to send a GET request. Redux Thunk allows us to dispatch those actions asynchronously and resolve each promise that gets returned.

#### other

- React routing vs conventional routing
- React styling / inline , css , js object, styled component
- Server Side rendering and client side rendering
- Pure functions
- What do you understand by refs in React?
- Use cases of ref
  - Managing focus, text selection, or media playback.
  - Triggering imperative animations.
  - Integrating with third-party DOM libraries.
- How to handle many APIs in react
- How to handle API errors in one place

#### Articles to Refer

- [interview questions](https://www.sitepoint.com/react-interview-questions-solutions/)
