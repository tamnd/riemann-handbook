---
id: unf-k
title: Unfolding the second-orbit term of the Eisenstein series
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Act.C5.unf_k
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.ThetaParseval.ThetaKernels.UnfK
covers: 301
status: drafted
drafted_by: writer@claude
---
This theorem does the analytic work of [the second-orbit unfolding](/entry/sec-unf-of-c-law-k/). It takes the part of a Fourier coefficient of the Siegel Eisenstein series that comes from the cosets outside the first orbit, and it writes that part as a constant times a Fourier coefficient on a group of lower rank. It is the `_k` copy of [the unfolding lemma](/entry/unf/), with `GoodK` in place of `IsGood` (see [the Siegel-Weil entry](/entry/siegel-weil-std-k/)). It belongs to the [Siegel-Weil chapter](/proof/siegel-weil/).

## Statement

**Theorem.** Let $d$ be a Siegel-Weil datum with the extra data `RD_k`, let $L$ be a datum of lower rank, and let $f$ be a section of the induced representation at $s_1$. Fix $z \in \mathbb{C}$. Assume:

1. coefficient data for $d$ and for $L$ (a coordinate map $nb$ of the unipotent radical, a Haar measure $\lambda$ and a fundamental domain $\mathcal{G}$ of volume one);
2. data for the unipotent map $u_M$ with measure $\nu$ on a domain $\mathcal{U}$;
3. the character $T$ is zero in row and column $i_0$, and $T'$ is the matrix that is left;
4. the integrability and summability conditions `habs`;
5. the hypothesis `Hyp_k` on a rational Weyl-type element $w_1$ and a block upper-triangular map $c_M$;
6. $c_M$ is continuous and $\kappa$ is an additive Haar measure.

Then there is $K \in \mathbb{C}$ such that for all $x$,
$$\mathrm{second}(x) = K \sum_{q'} \int_{\mathcal{G}'} \Big( \int \phi_z\big(w_1\, c_M(c)\, j(\mathrm{rep}(q')\, nb'(\beta))\, x\big)\, d\kappa(c) \Big)\, \psi(-\mathrm{tr}(T'\beta))\, d\lambda'(\beta).$$
Here $q'$ runs over the rational cosets of the Siegel parabolic of $L$, and $\phi_z(y) = \mathrm{Ht}(y)^{z - s_1} f(y)$.

## Proof

1. The rational points and the cosets are countable.
2. `pEquiv_k` splits the unipotent radical of $d$ into three coordinates. `lam_map_k` and `kap_eq_k` show that $\lambda$ and $\kappa$ change by constants $c_P$ and $c_K$.
3. `exists_fd_fA` gives a fundamental domain for $F$ in $\mathbb{A}_F$.
4. `second_orbit_bijection` matches the cosets outside the first orbit with pairs of a coset $q'$ of $L$ and a rational point $c$. Each representative has the form $p\, w_1\, c_M(c)\, j(\mathrm{rep}(q'))$ with $p$ in the rational Siegel parabolic.
5. `second_orbit_section_integral` and `eisenstein_second_term_expand` write the term as one integral of a sum over this sigma type.
6. Fubini (`hasSum_integral_of_summable_integral_norm`, `tsum_sigma`, `Act.exch`) exchanges the sum and the integral. The bound comes from `habs`.
7. `unfqE_k` and `unfqC_k` fold the sum over rational $c$ and the integral over the fundamental domains into one integral over $\nu \times \lambda_A$. This becomes the $\kappa$-integral.

The constant is $K = c_P \cdot c_K^{-1}$.

## In the Lean code

The theorem is in [UnfK.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/UnfK.lean#L32). `Hyp_k` is in [EisensteinSecondTerm.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/EisensteinSecondTerm.lean#L20), and `secondOrbitSection` is in [SiegelWeilActDefs.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilActDefs.lean#L28).

- The parent builds `Hyp_k` from `CLawEx_k` and gets `habs` from `AbsConv_k`.
- A second structure with the same name and the same fields is in [FirstOrbitParabolicLeft.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/FirstOrbitParabolicLeft.lean#L31), in namespace `C6`.
- The namespace name `C5` is not explained in the code.
- We have not unfolded `pEquiv_k`, `unfqE_k` or `unfqC_k`.
