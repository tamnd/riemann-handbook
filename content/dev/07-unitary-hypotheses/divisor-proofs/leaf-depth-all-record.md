---
id: leaf-depth-all-record
title: The four leaf depth bounds at a record
kind: theorem
decl: GlobalTheory.BigOn.leafDepth_all_record
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.LeafDepthAllRecord
covers: 4843
status: drafted
drafted_by: writer@claude
---
This theorem gives four bounds on the local depths of a leaf object that is a record of a run. It is [the same bounds for a run](/entry/leaf-depth-all-run/), with its three chart hypotheses proved and its run hypothesis read off from the record. The real content is in that entry. The only user is [the geometric statement from the page statement](/entry/geo-st-of-page-st-alt/), in branch 2 of [the unitary hypotheses](/proof/unitary-hypotheses/).

## Statement

There is a constant $C_0$ with this property. Let $D$ be a datum with size data $L$, a parameter choice and the other data of a run. Let $O$ be an object of the leaf (`OnObj`) and $N$ a numerical datum (`IndefNum`). Suppose:

1. $O$ is a record of the runs (`IsRec`);
2. `LeafPage O` (sign conditions, and four distinct primes $g_1, g_2, q_1, d$ outside a finite set $s$ of small primes) and `LeafSizes O` (such as $1 < Y \le mb$);
3. $x \ge 3$, $k b' \le b$ and $x^{e_z/5} \ge 3$ for the sizes in $L$, and $C_W \ge 10$ for the parameter choice;
4. the content $F_0$ of $N$ equals the content of the datum (`ContentEqualsDatumContent`);
5. $C_0 \le C$, where $C$ is the constant of $O$.

Then four depth bounds hold. In them $w$ is a twisted place with residue characteristic $p_w$ and conjugate $\bar w$, $j$ is an index, and $e_0(w, j)$ is a depth field of $O$, which we did not unfold.

- (`LeafDepthGood`) for $p_w$ not special and $p_w \le Y$, $e_0(w, j)$ and $e_0(\bar w, j)$ are at most $F_0(w, j) + a(j, p_w) + 1$, for a family $a \ge 0$ with a bound on $\sum_l a_l \log l$. For $p_w > Y$ both depths are $0$.
- (`LeafDepthRam`) for $p_w \in \{q_1, d\}$, both depths are at most $s_B(j) + T + 1$, with bounds on $F_0(w, j)$.
- (`LeafDepth2`) for $p_w \in s$, both depths are at most $s_C(j) + T + 1$ and $F_0(w, j) = 0$.
- (`LeafDepthLevel`) for $p_w \in \{g_1, g_2\}$, $e_0(w, j) \le 2T - n(w, j)$, the same for $\bar w$, and $n(w, j) + n(\bar w, j) = -2F_0(w, j)$.

## Proof

`leafDepth_all_run` takes three statements on charts of formal groups, for every prime $p$: `AvFSt p`, `HTFSt p` and `UpFSt p`. By their names, they are a colength bound at split places, a Hodge-Tate inclusion and a bound for unramified companions. The proof supplies `colength_bound_split_place_chart`, `hodgeTate_inclusion_chart` and `unramified_companion_chart_characters`, and gets $C_0$.

The field `depth` of the record gives a star structure and the run tie `RunTie`. The field `tied` gives the laws `LawsCore`, which `toLawsM` turns into `LawsM`. The rest is bookkeeping.

## In the Lean code

The theorem is in [LeafDepthAllRecord.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LeafDepthAllRecord.lean#L17). It calls `GlobalTheory.RunDepth.leafDepth_all_run` in [LeafDepthAllRun.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/LeafDepthAllRun.lean#L13) and the three chart theorems in the folder `UnramifiedDepth`. `IsRec` is in [RealisedChainTorusEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RealisedChainTorusEq.lean#L55).

The proof is a pass-through. Of the nine fields of `IsRec` it uses two. The other fields (`ok`, `kap`, `DF_eq`, `rr_eq`, `Nc_eq`, `realisedChain_torus_eq`, `pde_eq`) are not used.
