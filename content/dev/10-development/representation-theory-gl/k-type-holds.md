---
id: k-type-holds
title: A Whittaker generic module with integral infinitesimal character has an invariant tensor
kind: theorem
decl: PositivityTheory.Rg.Cz.kType_holds
module: Development.WeilBound.RepresentationTheoryGL.CasimirAlgebra.TensorRelationsGL.KTypeHolds
covers: 426
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `KType`. It is a fact about a module with several commuting actions of $\mathfrak{gl}_n$ and a compact group. If the module has an integral infinitesimal character and a Whittaker functional, then a twisted tensor power of it has a nonzero invariant vector with a given column shape. The proof is a chain of 24 lemmas. It sits below [the step EveryCharacter](/step/every-character/).

## Statement

Take $n \geq 1$, a complex vector space $M$, a finite set $\iota$ with an involution $\tau \mapsto \bar\tau$ without fixed points, and a compact group $\Gamma$. The data are:

- for each $\tau$, a continuous unitary representation $\kappa_\tau : \Gamma \to U(n)$, with $\kappa_{\bar\tau} = \overline{\kappa_\tau}$ and the $\kappa_\tau$ jointly injective (`IsKD`);
- for each $\tau$, operators $E_\tau(a,b)$ on $M$ that satisfy the $\mathfrak{gl}_n$ relations (`GlRel`) and commute for different $\tau$;
- an action $\rho$ of $\Gamma$ on $M$ that is locally finite, moves $E_\tau$ by $\kappa_\tau$, and has derivative $E_\tau(X) + E_{\bar\tau}(\bar X)$ in the direction of a skew-hermitian $X$ (`IsGK`).

Assume that for each $\tau$ there is an injective $l_\tau \in \mathbb{Z}^n$ such that the quantum determinant of $E_\tau$ acts as the scalar $\prod_k (u + l_\tau(k))$ (`HasChar`). Assume that a nonzero functional $\ell$ satisfies $\ell \circ E_\tau(a,b) = \psi(a,b)\,\ell$ for $a < b$, with $\psi$ nonzero just above the diagonal and zero further up (`IsWh`).

**Theorem.** There is $s \in \mathbb{Z}$ with `KTypeData`. That is, there are $q$ boxes with labels in $\iota$, $N$ further labels $t_k$ with $t_k \neq \bar t_{k'}$, a tableau (`IsTab`: each box has a column and a row, no two boxes share both, and each column fills the rows from some row down to the last row) and a vector $\eta \in M \otimes (\mathbb{C}^n)^{\otimes(q+2N)}$ such that:

- $s - l_\tau(w(i))$ equals the number of boxes with label $\tau$ in row $i$, plus $i$, for some permutation $w$;
- $\eta$ is fixed by $\Gamma$, which acts on the tensor slots through the $\kappa$ of their labels, the last $N$ slots with $\bar t_k$;
- $\eta$ is antisymmetric along each column;
- `altPair` $\eta \neq 0$.

The quantum determinant is the one of [StatementE.lean](lean:Formalism/RealPlaceAnalysis/StatementE.lean#L17). We did not unfold it.

## Proof

The proof builds lemmas in order, with `curry_holds` and `qdetFacts_holds` as side inputs: `tensorGl_holds` (the $\mathfrak{gl}_n$ relations on $M \otimes (\mathbb{C}^n)^{\otimes P}$), `jmComm_of` (the elements `xJ`, of Jucys-Murphy form, commute), `piQdet_of`, `stepFormula_of`, `stepChar_of`, `spectrum_of`, `height_of`, `wallQuot_of`, `chain_of`, `colAnti_of`, `transFin_of`, `trans_of`, `transAll_of`, `tensorGK_of`, `wallAlg_of`, `lieInv_holds`, `contract_of`, `semiZero_of` and `sphAll_of`. The last one gives `SphAll`: a nonzero functional on which the quantum determinant acts by $(u+s)^n$ sees a $\Gamma$-fixed vector. Then `kType_of` combines `TensorGl`, `TransAll`, `TensorGK`, `SphAll` and `young_holds`. It sorts the $l_\tau$ (`sort_data`), picks one of each pair $\{\tau, \bar\tau\}$ (`half`), and builds the tableau from the sorted values.

## In the Lean code

The theorem is in [KTypeHolds.lean](lean:Development/WeilBound/RepresentationTheoryGL/CasimirAlgebra/TensorRelationsGL/KTypeHolds.lean#L27). `KType` is in [StepFormula.lean](lean:Development/WeilBound/RepresentationTheoryGL/CasimirAlgebra/TensorRelationsGL/StepFormula.lean#L81). `KTypeData`, `IsKD` and `IsGK` are in [KTypeData.lean](lean:Development/WeilBound/RepresentationTheoryGL/CasimirAlgebra/TensorRelationsGL/KTypeData.lean#L102). We read `kType_of` only at its start. We did not open the other lemmas.

Two users apply it: `clozelCohomological_of_rest` in `CasimirAlgebra/KugaCoordinates/ClozelCohomologicalOfThree.lean` (line 11), and `GSp4Splitting.lowType` in `LowType.lean` (line 55). The second takes $M$ from a cuspidal representation of $\mathrm{GL}_n$ over a totally complex field, with $\iota$ the embeddings into $\mathbb{C}$.
