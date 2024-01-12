import React from "react";
import Container from "./container";

export default function Footer() {
  return (
    <div className="relative">
      <Container>
        <div className="my-10 text-sm text-center text-blue-200 dark:text-gray-400">
          Certibot © {new Date().getFullYear()}
        </div>
      </Container>
    </div>
  );
}
