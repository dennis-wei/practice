defmodule AppleOrange do
  @moduledoc """
  Documentation for AppleOrange.
  """

  @doc """
  main

  Input: newline separated values according to problem specifications

  Output:
    One line denoting the number of apples that fall onthe house
    One line denoting the number of oranges that fall onthe house
  """
  def main(input) do
    tokens = input |> String.split("\n")
    [s, t] = List.pop_at(tokens, 0) |> elem(0) |> String.split(" ") |> Enum.map(&String.to_integer(&1))
    [a, b] = List.pop_at(tokens, 1) |> elem(0) |> String.split(" ") |> Enum.map(&String.to_integer(&1))
    apples_list = List.pop_at(tokens, 3) |> elem(0) |> String.split(" ") |> Enum.map(&String.to_integer(&1))
    oranges_list = List.pop_at(tokens, 4) |> elem(0) |> String.split(" ") |> Enum.map(&String.to_integer(&1))

    apples_on_house = apples_list
      |> Enum.map(&(&1 + a))
      |> Enum.reduce(0,
        fn(x,y) ->
          cond do
            s <= x && x <= t -> y + 1
            true -> y
          end
        end)
    
    oranges_on_house = oranges_list
    |> Enum.map(&(&1 + b))
    |> Enum.reduce(0,
      fn(x,y) ->
        cond do
          s <= x && x <= t -> y + 1
          true -> y
        end
      end)
    
    Integer.to_string(apples_on_house) <> "\n" <> Integer.to_string(oranges_on_house)
  end
end
