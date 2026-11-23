---
id: unf
title: Unfolding the second orbit term of the Eisenstein series
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Act.C5.unf
module: Development.WeilBound.CoreStatements.AutomorphicKernels.SiegelWeilFormula.SiegelWeilActions.ImportsAlt
covers: 302
status: drafted
drafted_by: writer@claude
---
This theorem does the analytic work of [the second orbit unfolding](/entry/sec-unf-of-c-law/). It writes the non-Lagrangian part of a Fourier coefficient of the Siegel Eisenstein series as a constant times a Fourier coefficient of a coset sum on the group of lower rank. The result goes to the constant term split `CTSplit` in Step 5 of the [Siegel-Weil chapter](/proof/siegel-weil/). Below it are 302 declarations.

## Statement

Let $d$ be a Siegel-Weil datum with group $G$, frame $b$ and character $\psi$, let $R$ be extra data `RD d`, and let $L$ be a lower rank datum with group $G'$, embedding $j \colon G' \to G$ and index $i_0$. Let $f$ be a section at $s_1$ (`IsSec`), $z \in \mathbb{C}$, and $\varphi_z(x) = \mathrm{Ht}(x)^{z - s_1} f(x)$ (`phz`). For $T$ in the rational points of the unipotent radical, put $\psi_T(\beta) = \psi(-\operatorname{Tr}_{\mathbb{A}_E/\mathbb{A}_F} \operatorname{tr}(T\beta))$. Call a rational $\gamma$ *Lagrangian* (`LagrangianCondition`) if column $i_0$ of the lower left block of its frame matrix is 0. The second orbit term is

$$c_2(x) = \sum_{\gamma \text{ not Lagrangian}} \int_{\mathcal{U}} \int_{\mathcal{G}} \varphi_z\bigl(\gamma\, n(\beta)\, u_M(u)\, x\bigr)\, \psi_T(\beta)\, d\lambda(\beta)\, d\nu(u),$$

with $\gamma$ over the cosets of `par2` in `rat2` (`sec2`).

**Theorem.** Assume:

1. `CoefData` for $(n, \lambda, \mathcal{G})$ on $d$ and $(n', \lambda', \mathcal{G}')$ on $L$: $n(\beta)$ has frame matrix $\begin{pmatrix} 1 & \beta \\ 0 & 1 \end{pmatrix}$, and $\mathcal{G}$ is a fundamental domain of Haar measure 1 for the rational points;
2. `UData` for $(u_M, \nu, \mathcal{U})$, and $T$ is 0 in row and column $i_0$ with $T'$ the rest (`IsSub`);
3. for each $x$, each term of $c_2(x)$ is absolutely integrable and the absolute integrals are summable over all cosets;
4. `Hyp` for a rational element $w_1$ and a map $c_M$, with $c_M$ continuous and $\kappa$ an additive Haar measure.

Then there is $K \in \mathbb{C}$ such that for each $x$

$$c_2(x) = K \sum_{q'} \int_{\mathcal{G}'} \Bigl(\int \varphi_z\bigl(w_1\, c_M(c)\, j(q'\, n'(\beta))\, x\bigr)\, d\kappa(c)\Bigr)\, \psi_{T'}(\beta)\, d\lambda'(\beta),$$

with $q'$ over the lower rank cosets. `Hyp` says: $w_1$ is the identity in the frame except for the block $\begin{pmatrix} 0 & a \\ b & 0 \end{pmatrix}$ at the two positions $i_0$, with $a, b \neq 0$; for some $\delta \neq 0$, $c_M(u, r)$ is block upper triangular with upper blocks $1 + \sum_j u_j e_{i_0, e(j)}$ and $r\delta\, e_{i_0 i_0}$.

## Proof

1. `pEquiv` splits the unipotent radical as $\mathbb{A}_E^{n-1} \times \mathbb{A}_F \times N'$, and the rational points split the same way. By `lam_map` and `kap_eq`, $\lambda$ and $\kappa$ go to product Haar measures up to constants $c_P$ and $c_K$.
2. `non_lagrangian_cosets_bijection` matches the non-Lagrangian cosets with pairs $(q', c_0)$ of a lower rank coset and a rational point $c_0$ (`Crat`). Each representative is $p\, w_1\, c_M(c_0)\, j(q')$ with $p$ rational in the parabolic.
3. `section_sum_integral_expand` writes $c_2(x)$ as one integral of a coset sum. `coordsC` changes coordinates by step 1, and `eisenstein_term_expansion` rewrites the sum by step 2. Fubini and Tonelli (`coordsE`, `exch`) exchange the sums and the integral.
4. For each $q'$, `unfqE` and `unfqC` fold the sum over $c_0$ and the integral over the fundamental domains into one integral over $\mathbb{A}_E^{n-1} \times \mathbb{A}_F$. This is the $\kappa$-integral up to $c_K$.

So $K = c_P / c_K$. The rest is bookkeeping.

## In the Lean code

The theorem is in [ImportsAlt.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/ImportsAlt.lean#L21). `Hyp` is in [EllA.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/EllA.lean#L18), and `sec2` in [LagrangianCondition.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/LagrangianCondition.lean#L31).

- A structure `C6.Hyp` with the same fields is in [PartialDerivativeAlgebra.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/PartialDerivativeAlgebra.lean#L27). `non_lagrangian_cosets_bijection` builds a `C6.Hyp` from the fields of `h`.
- The `IsNMap` facts are given twice: in `hc`, `hc'` and in `h`.
- We have not unfolded `pEquiv`, `coordsC`, `unfqE` or `unfqC`.
- The copy [`unf_k`](/entry/unf-k/) has the same form.
