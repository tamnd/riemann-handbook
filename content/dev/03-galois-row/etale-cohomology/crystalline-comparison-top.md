---
id: crystalline-comparison-top
title: A Frobenius relation on crystalline periods, from two comparison inputs
kind: theorem
decl: UpperTheory.Ru.crystallineComparison.top
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.PhiHIterSmul
covers: 543
status: drafted
drafted_by: writer@claude
---
This theorem proves the Frobenius relation of Eichler-Shimura type that [the Frobenius step](/entry/phi-step/) uses, under two hypotheses on a map from étale to crystalline cohomology. Its only user is [`final`](/entry/final/), which proves these hypotheses and the finiteness conditions on the model. The relation goes up through [`finAll_of`](/entry/fin-all-of/) and [`finAll`](/entry/fin-all/).

## Statement

Let $K \subset \overline{\mathbb{Q}}_\ell$ be a field whose ring of integers $\mathcal{O}_K$ is a discrete valuation ring with uniformizer $\varpi$. Let $X \to \operatorname{Spec} \mathcal{O}_K$ be smooth and quasi-compact, with $X$ covered by finitely many affines (`AffFin`). Write $V = H^j(X_{\overline{K}}, \mathbb{Q}_\ell)$ with its action of $G_K$. Let $f > 0$ and let $T_0, \dots, T_n$ be correspondences $X \xleftarrow{p} Z_i \xrightarrow{r} X$ over $\mathcal{O}_K$, with $p$ finite of degree $d_i$ and étale where $\ell$ is invertible. Assume the point identity `PtId`: at valuation-ring points that reduce to a generic point of the special fibre, the reductions of the points of $Z_i$ satisfy an alternating identity `AltId` with the $\ell^f$-power Frobenius (not unfolded). Let $A_i$ be the action of $T_i$ on $V$ (`IsHk`).

Let $c \colon A_{\mathrm{cris}} \to C$ be a ring map, compatible with a Frobenius $\varphi$ and a $G_K$-action, such that $c(t)$ is a unit, each element is $c(a)/c(t)^r$, and $\ker c$ is the $t$-power torsion. So $C = A_{\mathrm{cris}}[1/t]$. Let $e$ be a natural, Frobenius-compatible family of maps from the levels of an integral form `M.T j` of $V$ to the $A_{\mathrm{cris}}$-cohomology `MH` of $X$ (`EtFam`, `Good`). We have not unfolded `M.T j` or `MH`.

**Theorem.** Assume:

1. (`InjE`) a vector $\sum_k v_k \otimes c(c_k)$ of $V \otimes C$ is $0$ when $t^u \sum_k c_k\, e(v_k) = 0$ at all levels;
2. (`AbsInv`) for each $G_K$-invariant $\sum_k v_k \otimes c(c_k)/c(t)^r$ there is, at each level, a class $y$ of the special fibre (over a residue map with values in $\mathbb{F}_{\ell^f}$) with $\varphi^f y = F^* y$ for the $\ell^f$-power Frobenius $F$, and $\ell^a t^u \sum_k \varphi^{fN_1}(c_k)\, e(v_k) = t^{u+r} \rho^* y$ for the reduction map $\rho$.

Then there is $N$ such that for each $G_K$-invariant $x \in V \otimes C$
$$\sum_{i=0}^{n} (-1)^i (\ell^f)^{\binom{i}{2}} \bigl(A_i \otimes \varphi^{f(n-i+N)}\bigr) x = 0.$$

## Proof

1. `wEx` gives a cover $\pi \colon W \to X$ on which each $T_i$ splits into $d_i$ sections where $\ell$ is invertible.
2. `wZero` turns `PtId` into a vanishing relation `TZero` on the special fibre: the alternating sum of the sections, composed with $\rho$ and powers $F^{n-i+N_0}$ of Frobenius, is $0$. `siteAnn` applies it to the class $y$ of hypothesis 2.
3. `exists_crystalline_lattice_expansion` writes $x$ as $\sum_k v_k \otimes c(c_k)/c(t)^r$. `hecke_correspondence_product` writes $A_i$ on the lattice through the sections, up to powers of $\ell$.
4. `levZero` combines these. It moves $\varphi^m$ through the sums (`phiH_iter_smul`, and $\varphi(t) = \ell t$). A transfer (`wTrans`, `avgMH`) shows that pullback to $W$ kills only classes killed by $|\prod_i S_{d_i}|$. The result is $t^u \sum e(\cdot) = 0$ at all levels, for $\kappa$ times the relation, with $\kappa = |\prod_i S_{d_i}| \cdot \ell^{a'}$.
5. Hypothesis 1 moves this to $V \otimes C$, and `crystalline_expansion_relation_of_scaled_endomorphisms` divides by $\kappa \neq 0$. Here $N = N_0 + N_1$.

## In the Lean code

The theorem is in [PhiHIterSmul.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/PhiHIterSmul.lean#L179). `Top`, `InjE` and `AbsInv` are in [VecZero.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/VecZero.lean#L87). We have not read the proofs of `wZero` and `wEx`.

- The file is named after the helper lemma `phiH_iter_smul`.
- Each hypothesis is used. `Top` does not assume $[K : \mathbb{Q}_\ell] < \infty$; `final` does.
- If `Acris` and `tA` are the standard $A_{\mathrm{cris}}$ and $t$, then $C$ is Fontaine's $B_{\mathrm{cris}}$ (Astérisque 223, 1994). We have not unfolded `Acris`.
