defmodule CamelCaseTest do
  use ExUnit.Case
  doctest CamelCase

  test "given test" do
    assert CamelCase.main("saveChangesInTheEditor") == 5
  end
end
