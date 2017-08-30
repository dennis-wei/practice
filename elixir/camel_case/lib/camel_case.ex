defmodule CamelCase do
  @moduledoc """
  Documentation for CamelCase.
  """

  @doc """
  main

  Input: A camel case string

  Output: The number of words in that string
  """
  def main(input) do
    input
      |> to_charlist
      |> count_words
  end

  def count_words(input) do
    input
      |> Enum.reduce(0, &(is_upper(&1, &2)))
      |> Kernel.+1
  end

  def is_upper(input_char, count) do
    match = [input_char] |> to_string
    if match =~ ~r/^\p{Lu}$/u do
      count + 1
    else
      count
    end
  end
end
