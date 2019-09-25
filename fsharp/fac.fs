// Learn more about F# at http://fsharp.org

open System

let fac n =
        seq { 1..n }
        |> Seq.map bigint
        |> Seq.reduce(*)

[<EntryPoint>]
let main argv =
    let res = seq { 1..3000 } |> Seq.map fac |> Seq.sum
    printf "%A" res
    0 // return an integer exit code
