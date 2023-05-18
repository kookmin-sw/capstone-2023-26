/** @jsxImportSource @emotion/react */
import { css } from "@emotion/react";

const defaultProps = {
  width: "auto",
  height: "auto",
  margin: "0",
  padding: "0",
  gap: "0",
  borderRadius: "",
  column: false,
  reverse: false,
  wrap: "nowrap",
  justifyContent: "flex-start",
  alignItems: "flex-start",
  center: false,
  background: "transparent",
  position: "static",
  top: "0",
  right: "0",
  borderBottom: "0",
  color: "black",
  boxShadow: "0",
};

const FlexBox = (props) => {
  const {
    children,
    width,
    height,
    margin,
    padding,
    gap,
    borderRadius,
    column,
    reverse,
    wrap,
    justifyContent,
    alignItems,
    center,
    background,
    position,
    right,
    top,
    borderBottom,
    color,
    boxShadow,
    onClick,
  } = props;

  const dir = (column ? "column" : "row") + (reverse ? "-reverse" : "");

  return (
    <div
      css={css`
        display: flex;
        width: ${width};
        height: ${height};
        margin: ${margin};
        padding: ${padding};
        border-radius: ${borderRadius};
        flex-direction: ${dir};
        flex-wrap: ${wrap};
        justify-content: ${center ? "center" : justifyContent};
        align-items: ${center ? "center" : alignItems};
        background-color: ${background};
        position: ${position};
        top: ${top};
        right: ${right};
        gap: ${gap};
        border-bottom: ${borderBottom};
        color: ${color};
        box-shadow: ${boxShadow};
      `}
      onClick={onClick}
    >
      {children}
    </div>
  );
};
FlexBox.defaultProps = defaultProps;

export default FlexBox;