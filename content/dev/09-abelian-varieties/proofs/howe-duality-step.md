---
id: howe-duality-step
title: The inductive step for the unramified Howe statement
kind: theorem
decl: GlobalTheory.Hk3.HoweDuality.step
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.RhoMemOfMkEq
covers: 319
status: drafted
drafted_by: writer@claude
---
This lemma is the inductive step in [fixed-mem-span](/entry/fixed-mem-span/). It supplies the last hypothesis of the abstract lemma there: an orbit of classes that carries a fixed vector also carries a vector of $S$, modulo lower height. The notation is the notation of fixed-mem-span and [howe-unram-holds](/entry/howe-unram-holds/).

## Statement

Take the data of a `LocPair`, a vacuum vector $s \neq 0$, and suppose that the vectors $\rho(x)s$ span $M$. Let $x \in \mathrm{Mat}_{n' \times n}(L)$, and let
$$O_x = \operatorname{span}\{\rho(hx)s : h \in K_T\}.$$
Suppose that $O_x$ contains a nonzero vector fixed by $\omega(1, k)$ for every $k \in K_T$. Then there are $v \in S$ and a vector $u$ in the span of the $\rho(y)s$ with $\mu(y) < \mu(x)$, such that $v - u$ is a nonzero element of $O_x$. Here $\mu$ is the lattice index `latIdx` and $S$ is the span of the $\omega(g,1)s$, $g \in U(J_S)$.

## Proof

The proof has three moves.

1. `exists_int_gram_of_fixed_alt` uses the fixed vector to find an integral matrix $l$ such that $(x - l) J_S^{-1} ((x - l)^\sigma)^{T}$ is integral. So after an integral shift, $x$ has an integral Gram matrix.
2. `exists_conjugateModel_extremal_dual_parameter` takes any matrix with an integral Gram matrix. Applied to $x - l$, it gives $v \in S$ and $u$ of height below $\mu(x - l)$, with $v - u$ a nonzero element of $O_{x-l}$.
3. The proof moves back from $x - l$ to $x$. The height does not change under integral translation, so $\mu(x - l) = \mu(x)$. For $h \in K_T$, $hl$ is integral, so $h(x - l)$ and $hx$ have the same class. Then `rho_mem_of_mk_eq` puts $\rho(h(x-l))s$ in the line of $\rho(hx)s$. So $O_{x-l} \subseteq O_x$.

The real content is in the two lemmas of moves 1 and 2. They are proved by `HoweDuality.exists_int_gram_of_fixed` and `HoweG.gramClass_orbit_mod_lower`. We read their statements only. The second lemma does not use any fixed vector. So the fixed vector is used only to make the Gram matrix integral.

## In the Lean code

The lemma is in [RhoMemOfMkEq.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/RhoMemOfMkEq.lean#L107). The two statements are in [ExistsIntGramOfFixedStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsIntGramOfFixedStatement.lean#L7) and [ExistsConjugateModelExtremalDualParameterStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsConjugateModelExtremalDualParameterStatement.lean#L7). Both are renamings, by `first | exact`, of the lemmas named above. The name of the second one does not say what it states.
