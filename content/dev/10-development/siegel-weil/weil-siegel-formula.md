---
id: weil-siegel-formula
title: The Siegel-Weil formula in the convergent range
kind: theorem
decl: PositivityTheory.Rg.Wsf.weilSiegelFormula
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeil.ArchimedeanSiegelWeil.WeilSiegelFormula
covers: 1728
status: drafted
drafted_by: writer@claude
---
This theorem proves `WeilSiegelFormula`, the Siegel-Weil formula for $2n < m$ at the identity. [`weilUnitary`](/entry/weil-unitary/) gets its third part from it. The proof reduces it to one identity for each Hermitian $\beta$ and takes the case $\det \beta = 0$ from [`siegelDeg`](/entry/siegel-deg/), which covers 1,490 of the 1,728 declarations.

## Statement

Let $D$ be a `D7` datum, with CM extension $E/F$ (`isCMExt_D`). Write $x^*$ for the conjugate transpose, $\operatorname{Tr}$ for the trace $\mathbb{A}_E \to \mathbb{A}_F$ and $\operatorname{tr}$ for the matrix trace. Let $V$ be a Hermitian space of rank $m$ with Gram matrix $J$, and $[\mathrm{U}(V)] = \mathrm{U}(V)(F) \backslash \mathrm{U}(V)(\mathbb{A})$. Let $G$ be the unitary group of $J_n = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ over $\mathbb{A}_E$, and $P$ its Siegel parabolic.

**Theorem.** Let $n \geq 1$ with $2n < m$. Let $\psi$ be a nontrivial unitary character of $\mathbb{A}_F / F$ (`IsCharAF`). Let $\chi$ be a unitary character of $\mathbb{A}_E^\times / E^\times$ with $\chi|_{\mathbb{A}_F^\times} = \eta^m$, where $\eta$ is any nontrivial character of $\mathbb{A}_F^\times / F^\times$ trivial on norms (`IsHeckeChar`, `ResEta`). Let $S$ be the Schwartz space `schwartzA θ m n` on $M_{m \times n}(\mathbb{A}_E)$, with `IsInfFam θ`. Let $\mu$ be a measure on $M_{m \times n}(\mathbb{A}_E)$ of covolume $1$ for $M_{m \times n}(E)$, and $\nu$ a Haar measure on $\mathrm{U}(V)(\mathbb{A})$. Let $\omega \colon G \to \operatorname{End}(S)$ be a homomorphism with the formulas of the Schrödinger model (`IsWeilSch`):
$$\omega\begin{pmatrix} a & 0 \\ 0 & (a^*)^{-1} \end{pmatrix}\Phi(x) = \chi(\det a)\lvert \det a \rvert^{m/2}\Phi(xa), \qquad \omega\begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}\Phi(x) = \psi\bigl(\tfrac12 \operatorname{Tr}\operatorname{tr}(b\,x^* J x)\bigr)\Phi(x),$$
and $\omega(J_n)\Phi(x) = \int \Phi(y)\,\psi(\operatorname{Tr}\operatorname{tr}(x^* J y))\,d\mu(y)$. Then for each $\Phi \in S$,
$$\sum_{\gamma \in P(F) \backslash G(F)} (\omega(\gamma)\Phi)(0) = \frac{1}{\operatorname{vol}[\mathrm{U}(V)]} \int_{[\mathrm{U}(V)]} \sum_{\xi \in M_{m \times n}(E)} \Phi(h^{-1}\xi)\,dh.$$

The two sides are the [[Eisenstein series|3NZBZXYWAJ]] at $g = 1$ and the normalized theta integral of the [[Weil representation|H3Q2703KKV]] $\omega$. This is the Siegel-Weil formula of Weil (Acta Math. 113, 1965) for $\mathrm{U}(n,n) \times \mathrm{U}(V)$ where both sides converge absolutely; see [the Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula).

## Proof

The proof is `head_of_deg siegelDeg`. For $\varphi$ on $M_{m \times r}(\mathbb{A}_E)$ and $b \in \mathrm{Herm}_r$, put $J_\varphi(b) = \int \varphi(y)\,\psi(\tfrac12 \operatorname{Tr}\operatorname{tr}(b\,y^* J y))\,d\mu(y)$. Let $I_\varphi$ be the normalized integral over $[\mathrm{U}(V)]$ of $\sum_x \varphi(h^{-1}x)$, over the $x \in M_{m \times r}(E)$ of rank $r$. For a subspace $U \subseteq E^n$ with basis matrix $c_U$, put $\Phi_U(y) = \Phi(y c_U)$. `weilSiegelFormula_of_chapters_LI` compares:

1. the Eisenstein sum is $\sum_U \sum_{b \in \mathrm{Herm}_{\dim U}(E)} J_{\Phi_U}(b)$ (`eisCells`);
2. the theta integral is $\sum_U I_{\Phi_U}$ (`thetaOrbits`);
3. $\sum_b J_\varphi(b) = I_\varphi$ when $2r < m$ (`BigCell`).

It also uses `pullSchLI`, `weilThetaConvergence_of_siegelSet` and `weilEisensteinSiegelConvergence`. By their names (we have not unfolded them), the last two give absolute convergence.

`bigCell_of_poisson_siegel` proves step 3. With $\lambda$ a Haar measure of covolume $1$ on $\mathrm{Herm}_r(\mathbb{A})$ (`exists_isCovolOneH`), let $W_\varphi(\beta) = \int_{\mathrm{Herm}_r(\mathbb{A})} J_\varphi(b)\,\psi(-\tfrac12 \operatorname{Tr}\operatorname{tr}(\beta b))\,d\lambda(b)$, and let $I_\varphi(\beta)$ be the part of $I_\varphi$ with $x^* J x = \beta$. Poisson summation (`poissonHerm_main`) gives $\sum_b J_\varphi(b) = \sum_\beta W_\varphi(\beta)$, and `hasSum_IfrB` gives $I_\varphi = \sum_\beta I_\varphi(\beta)$. Then $I_\varphi(\beta) = W_\varphi(\beta)$ is `siegelND` for $\det \beta \neq 0$ and [`siegelDeg`](/entry/siegel-deg/) for $\det \beta = 0$.

## In the Lean code

The theorem is in [WeilSiegelFormula.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/WeilSiegelFormula.lean#L4). The statement is in [WeilSiegelFormula.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/WeilSiegelFormula.lean#L18), `IsWeilSch` in [SiegelWeilUnitarySchrodinger.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/SiegelWeil₂/SiegelWeilUnitarySchrodinger.lean#L55). The chain from `head_of_deg` to `head_of_two` in [HeadOfSiegel.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/WeilSiegelFormula/HeadOfSiegel.lean#L58) supplies the inputs above.

The Lean form differs from Weil's: it is stated at $g = 1$, and it uses the average over $[\mathrm{U}(V)]$, not a Tamagawa measure, so no constant appears. The left side is a `tsum` over chosen coset representatives, and the statement has no convergence hypothesis.
