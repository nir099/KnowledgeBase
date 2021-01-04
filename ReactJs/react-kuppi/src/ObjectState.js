import React, { useState } from "react";

const ObjectState = () => {
  const [obj, setObj] = useState({ count: 0, name: "Amal" });

  const increment = () => {
    setObj(prevObj => {
      return { ...prevObj, count: prevObj.count + 1 };
    });
  };

  return (
    <>
      <p>{obj.count}</p>
      <p>{obj.name}</p>
      <button onClick={() => increment()}>Increment</button>
    </>
  );
};

export default ObjectState;
