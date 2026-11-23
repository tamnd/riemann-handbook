---
id: siegel-deg
title: The Siegel-Weil identity for a singular Gram matrix
kind: theorem
decl: GlobalTheory.CompanionTheory.WeilSiegel.Deg.siegelDeg
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeil.ArchimedeanSiegelWeil.PlaceIntegrals.SiegelDeg
covers: 1490
status: drafted
drafted_by: writer@claude
---
This theorem proves `SiegelDeg`: for a singular Hermitian matrix $\beta$, the part of the theta integral with Gram matrix $\beta$ equals the Fourier transform $W_\varphi(\beta)$ defined below. With the nonsingular case `siegelND`, it gives the big cell identity in the proof of [the Siegel-Weil formula in the convergent range](/entry/weil-siegel-formula/). It reduces $\beta$ to a block normal form and then calls [`siegel_weil_rank_coefficient`](/entry/siegel-weil-rank-coefficient/), a restatement of [the case of a represented block matrix](/entry/siegel-frame/), which has most of the content.

## Statement

We use the notation of [the Siegel-Weil formula in the convergent range](/entry/weil-siegel-formula/): $D$, $F$, $E$, the Hermitian space $V$ of rank $m$ with Gram matrix $J$, and $\operatorname{Tr}$, $\operatorname{tr}$. Let $r \geq 0$ and let $\mathrm{Herm}_r(R)$ be the Hermitian $r \times r$ matrices over $R$. Let $\psi$, $\theta$, $\mu$ (now on $M_{m \times r}(\mathbb{A}_E)$) and $\nu$ be as there, let $\lambda$ be a Haar measure on $\mathrm{Herm}_r(\mathbb{A})$ with a fundamental domain of measure $1$ for $\mathrm{Herm}_r(E)$, and let $\varphi$ be a function on $M_{m \times r}(\mathbb{A}_E)$. The hypothesis `Hyp` says: $2r < m$, $\varphi$ is in the Schwartz space `schwartzA θ m r`, its absolute theta integral is finite, and the conditions on $\psi$, $\theta$, $\mu$, $\lambda$, $\nu$ hold. For $\beta \in \mathrm{Herm}_r(E)$ put
$$I_\varphi(\beta) = \frac{1}{\operatorname{vol}[\mathrm{U}(V)]} \int_{[\mathrm{U}(V)]} \sum_{\substack{x \in M_{m \times r}(E),\ \operatorname{rank} x = r \\ x^* J x = \beta}} \varphi(h^{-1}x)\,dh,$$
$$W_\varphi(\beta) = \int_{\mathrm{Herm}_r(\mathbb{A})} \int_{M_{m \times r}(\mathbb{A}_E)} \varphi(y)\,\psi\bigl(\tfrac12 \operatorname{Tr}\operatorname{tr}(b\,y^* J y)\bigr)\,d\mu(y)\;\psi\bigl(-\tfrac12 \operatorname{Tr}\operatorname{tr}(\beta b)\bigr)\,d\lambda(b).$$
These are `IfrB` and `W` in the Lean code.

**Theorem.** Under `Hyp`, if $\det \beta = 0$, then $I_\varphi(\beta) = W_\varphi(\beta)$.

## Proof

For an invertible $a \in \mathrm{GL}_r(E)$ put $\varphi_a(y) = \varphi(ya)$.

1. By `singular_hermitian_congruent_block_normal_form`, $\beta = a^* \gamma a$ with $a$ invertible and $\gamma = \begin{pmatrix} \gamma_0 & 0 \\ 0 & 0 \end{pmatrix}$, where $\gamma_0$ is an invertible $t \times t$ matrix and $t < r$. This is the predicate `IsBlockNF t γ`.
2. Both sides move in the same way under this change of variables: $I_\varphi(a^* \gamma a) = I_{\varphi_a}(\gamma)$ (`frame_integral_congruence_invariant`) and $W_\varphi(a^* \gamma a) = W_{\varphi_a}(\gamma)$ (`whittaker_coefficient_congruence_pullback`, which uses the covolume conditions on $\mu$ and $\lambda$).
3. `Hyp` holds for $\varphi_a$ (`hypotheses_preserved_by_linear_pullback`).
4. If $\gamma = x^* J x$ for some $x \in M_{m \times r}(E)$ of rank $r$, then [`siegel_weil_rank_coefficient`](/entry/siegel-weil-rank-coefficient/) gives $I_{\varphi_a}(\gamma) = W_{\varphi_a}(\gamma)$. If not, `frame_integral_eq_coefficient_nonrepresented` gives it. In that case the sum that defines $I_{\varphi_a}(\gamma)$ is empty, so the content of that lemma is $W_{\varphi_a}(\gamma) = 0$.

## In the Lean code

The theorem is in [SiegelDeg.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/SiegelDeg.lean#L17). The statement `SiegelDeg`, and `IfrB`, `W` and `Hyp`, are in [BigCellDefs.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/WeilSiegelTheta/BigCellDefs.lean#L72). `IsBlockNF` and the congruence $a^* \gamma a$ (`congrH`) are in [IsBlockNFZeroOne.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/IsBlockNFZeroOne.lean#L27).

The five lemmas of the proof, other than `siegel_weil_rank_coefficient`, are stated in files of `Development/AutomorphicSpectrum/Proofs/BlockDecomposition` whose names end in `Statement`. Each proof is one `first | exact …` that names a lemma of another namespace: `exists_congrH_isBlockNF`, `ifrB_congrH`, `W_congr`, `hyp_pull` and `NoFrame.noFrame`. We have not opened the proofs of these five.
