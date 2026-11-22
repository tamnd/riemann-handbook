---
id: torsor-point-of-ess-finite-type
title: A torsor over a noetherian normal model gets a point
kind: theorem
decl: GlobalTheory.KeyOriginNoeth.torsor_point_of_essFiniteType
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.TorsorPointOverStrictHenselisationNoetherianNorm
covers: 540
status: drafted
drafted_by: writer@claude
---
This theorem gives a point to a cyclic torsor that lives over a noetherian normal base, after base change to the generic fibre of the strict henselisation at the origin. It is restated as [the torsor point over a noetherian normal base](/entry/torsor-point-over-strict-henselisation-noetherian-normal/), which is step 3 of [`keyOrigin`](/entry/key-origin/). The proof enlarges the base until the torsor is good, and then uses that $O$ is strictly henselian.

## Statement

Let $T$ be a local domain that is absolutely integrally closed. Let $P = (\mathfrak{m}_T, X) \subset T[X]$, and let $\varphi \colon T[X]_P \to O$ be a strict henselisation: $O$ is henselian with separably closed residue field, and $\varphi$ is local and ind-étale. For a ring $R$ over a domain $B$, write $R_K = R[(B \setminus \{0\})^{-1}]$. Let $q > 0$ be a unit in $T$.

Let $A$ be a noetherian, integrally closed local domain, essentially of finite type over $\mathbb{Z}$, with an injective local map $i \colon A \to T$, and with $q$ a unit in $A$. Let $E_A$ be an étale $A[X]$-algebra and $Q_A$ a prime of $E_A$ over $(\mathfrak{m}_A, X)$. Put $R = (E_A)_{Q_A}$. Let $j_A \colon R \to O$ be a ring map whose restriction to $A[X]$ is $A[X] \xrightarrow{i} T[X] \to O$. Let $\psi_A \colon R_K \to O_K$ be a ring map whose restriction to $R$ is $j_A$ followed by $O \to O_K$. Let $D_A$ be a $\mathbb{Z}/q$-torsor over $R_K$ (as in [the triviality of torsors](/entry/torsor-trivial/)).

**Theorem.** There is a ring map $\sigma \colon D_A \to O_K$ with $\sigma|_{R_K} = \psi_A$.

## Proof

1. **Enlarge.** [The good enlargement](/entry/strict-henselisation-enlarge-good-at-origin/) gives new data $(A', E_A', Q_A', D_A')$ of the same kind, with $R' = (E_A')_{Q_A'}$, but with no map from $A'$ to $T$. It comes with a retraction $\rho' \colon R' \to A'$ of $A' \to R'$ whose kernel is $(X)$, maps $j_A' \colon R' \to O$ and $\psi_A' \colon R'_K \to O_K$, and maps $\beta \colon R_K \to R'_K$ and $h \colon D_A \to D_A'$. They satisfy $\psi_A' \circ \beta = \psi_A$, and $h$ lies over $\beta$. The new torsor $D_A'$ is *good* for $\rho'$. Let $C$ be the integral closure of $R'$ in $D_A'$. Good means: $C_{\mathfrak{p}}$ is étale over $R'_{\mathfrak{p}}$ for each prime $\mathfrak{p}$ of $R'$ with $\operatorname{ht}(\mathfrak{p} \cap A') \leq 1$, and there is a ring map $C \to \operatorname{Frac}(A')$ that restricts to $\rho'$ on $R'$.
2. **The closure is finite étale.** `integralClosure_finiteEtale_originKeyLemma_essFiniteType` turns goodness into: $C$ is finite, étale and nonzero over $R'$.
3. **A point.** $O$ is henselian with separably closed residue field, and $D_A'$ is finite over $R'_K$. So `exists_point_closureFiniteEtale_strictHenselian` gives $\sigma' \colon D_A' \to O_K$ with $\sigma'|_{R'_K} = \psi_A'$.
4. Put $\sigma = \sigma' \circ h$. Then $\sigma|_{R_K} = \sigma' \circ \beta = \psi_A' \circ \beta = \psi_A$.

## In the Lean code

The theorem is in [TorsorPointOverStrictHenselisationNoetherianNorm.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TorsorPointOverStrictHenselisationNoetherianNorm.lean#L13). The lemmas it calls:

- `GlobalTheory.T.strictHenselisation_enlarge_good_at_origin`.
- `GlobalTheory.T.integralClosure_finiteEtale_originKeyLemma_essFiniteType`, an alias of `GoodEtale.closure_finiteEtale`, which we have not opened.
- `GlobalTheory.T.exists_point_closureFiniteEtale_strictHenselian`, an alias of `KeyOriginNoeth.exists_point_of_closureFiniteEtale`, which we have not opened.

`Good`, `closure` and `ClosureFiniteEtale` are in [ClosureFiniteEtale.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ClosureFiniteEtale.lean#L32). The closure is taken in $D_A'$ along $R' \to R'_K \to D_A'$.

The hypotheses on $T$, $P$ and $\varphi$, and the maps $i$ and $j_A$, are used only to pass them to the enlargement. From $\varphi$, step 3 uses only that $O$ is strictly henselian. The point lemma in step 3 asks for no condition on $j_A'$, not even that it is local.
