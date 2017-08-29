defmodule BirthdayCakeCandles do
  @moduledoc """
  Documentation for BirthdayCakeCandles.
  """

  @doc """
  main

  Input: two lines
    1st line is length of list on following line
    2nd line is list of heights of candles
  
  Outputs:
    Number of candles that can be blown out
  """
  def main(input) do
    l = input
      |> String.split("\n")
      |> List.last
      |> String.split(" ")
      |> Enum.map(fn x -> String.to_integer(x) end) 
    m = Enum.max(l)
    List.foldl(l, 0, fn(x, acc) ->
      case x do
        ^m -> acc + 1
        _ -> acc
      end
    end)
  end
end
