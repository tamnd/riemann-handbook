---
title: Plurisubharmonic log determinants of eigenframes
decls:
  - GlobalTheory.CompanionTheory.Ar.Cusp.phi_isPsh_continuous
  - GlobalTheory.T.log_det_cusp_frame_plurisubharmonic
  - GlobalTheory.CompanionTheory.Relay.log_det_eigen_frame_plurisubharmonic
  - GlobalTheory.T.log_det_eigen_frame_plurisubharmonic
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Plurisubharmonic log determinants of eigenframes

This section proves that two functions on the base of a holomorphic family of Riemann lattices are plurisubharmonic: the log Gram determinant of a holomorphic eigenframe, and the sum of this function and the cusp weight. It also proves that the cusp weight is continuous. The first function is a potential of the Hodge metric on the eigen part of the Lie algebra, and the cusp weight is the correction of Section 3. So the result says that the corrected potential is still plurisubharmonic, which is what the positivity of the corrected metric needs. The result enters the comparison of cusp intersection numbers for good towers. For plurisubharmonic functions and positivity we use [metrics, curvature and positivity](/learn/positivity-resolution/#metrics-curvature-and-positivity).

### Definitions

We keep the notation of Section 3: $E$ is a CM field, $\sigma_\tau$ for $\tau \in \Psi$ is a CM type, $\Lambda$ is an $\mathcal{O}_E$-module with an alternating unimodular form, and a Riemann lattice $R$ on $\Lambda$ is a map $P : \Lambda \to \mathbb{C}^g$ with a hermitian form $\langle\ ,\ \rangle_R$ and an action of $\mathcal{O}_E$. For vectors $u_1, \dots, u_m$ we write $\operatorname{Gram}_R(u)$ for the matrix of the values $\langle u_a, u_c \rangle_R$.

**Definition 10.4.1.** Let $U \subseteq \mathbb{C}^n$ be open. A function $\varphi : U \to \mathbb{R}$ is plurisubharmonic on $U$ if it is upper semicontinuous on $U$ and, for all $z, w \in \mathbb{C}^n$ such that $z + \zeta w \in U$ for every $\lvert\zeta\rvert \leq 1$, the function $\zeta \mapsto \varphi(z + \zeta w)$ is integrable on the unit circle and
$$
\varphi(z) \leq \frac{1}{2\pi} \int_0^{2\pi} \varphi(z + \exp(i\theta) w)\, d\theta .
$$

A holomorphic family of Riemann lattices on $U$ is a map $t \mapsto R_t$ with a fixed form such that $t \mapsto P_t(x)$ is holomorphic on $U$ for every $x \in \Lambda$. A family of eigenframes is a family of holomorphic maps $b_{\tau,i} : U \to \mathbb{C}^g$, $i < m$, such that for each $t$ and $\tau$ the vectors $b_{\tau,i}(t)$ are a basis of the eigenspace of $\sigma_\tau$ for $R_t$. Its log determinant is
$$
\ell(t) = \sum_\tau \log \det \operatorname{Gram}_{R_t}(b_{\tau}(t)) .
$$

### One cusp

**Lemma 10.4.2 (One cusp).** Let $U$ be open, let $t \mapsto R_t$ be a holomorphic family of Riemann lattices on $U$ with a family of eigenframes $b$, and let $I$ be a submodule of $\Lambda$ that is a cusp for every $R_t$, $t \in U$. Then $\ell(t) - \log \operatorname{nz}_{R_t}(I)$ is plurisubharmonic on $U$, and $t \mapsto \operatorname{nz}_{R_t}(I)$ is continuous on $U$.

Lean: `GlobalTheory.CompanionTheory.Ar.Cusp.phi_isPsh_continuous` (also `GlobalTheory.T.log_det_cusp_frame_plurisubharmonic`, a second name).

*Proof.* If $U$ is empty there is nothing to prove, so fix $t_1 \in U$. Since $I$ is a nonzero isotropic submodule, there are $v_1, \dots, v_r \in I$ such that for every $t \in U$ the number $\operatorname{nz}_{R_t}(I)$ is computed with this family and is positive. Let $w_{\tau,a}(t)$ be the $\sigma_\tau$ component of $P_t(v_a)$ and let $c$ be the index of the span of the $v_a$ in $I$. The components of an isotropic family are linearly independent, so every $\det \operatorname{Gram}_{R_t}(w_\tau(t))$ is positive. By definition of $\operatorname{nz}$,
$$
\begin{aligned}
\ell(t) - \log \operatorname{nz}_{R_t}(I) = \sum_\tau \bigl(&\log \det \operatorname{Gram}(b_\tau(t)) \\
&- \log \det \operatorname{Gram}(w_\tau(t))\bigr) + \log c .
\end{aligned}
$$
Plurisubharmonicity is a local property, so fix $t_0 \in U$. Near $t_0$ the family has a holomorphic local quotient: a family $R'_t$ of Riemann lattices on a quotient lattice of $I^\perp / I$ and a holomorphic projection $q$ whose kernel is spanned by the components of $I$. The eigenframe of the quotient is related to $b$ by
$$
\det \operatorname{Gram}_{R_t}(b_\tau) = \det \operatorname{Gram}_{R_t}(w_\tau) \cdot \det \operatorname{Gram}_{R'_t}(q\, b'_\tau)
$$
for a holomorphic subframe $b'_\tau$ obtained from $b_\tau$ with holomorphic span coefficients. So each summand above is, near $t_0$, the log Gram determinant of a holomorphic frame, and is plurisubharmonic. A finite sum of plurisubharmonic functions plus a constant is plurisubharmonic. For the continuity, the entries of the hermitian matrix of $R_t$ and the vectors $w_{\tau,a}(t)$ are continuous, so the Gram determinants and their product divided by $c$ are continuous. $\square$

### The cusp weight

**Theorem 10.4.3 (Plurisubharmonic log determinant).** Let $U$ be open, and let $t \mapsto R_t$ be a holomorphic family of Riemann lattices on $U$ with a family of eigenframes $b$. Then:

1. $\ell$ is plurisubharmonic on $U$;
2. $\ell + w(R_t)$ is plurisubharmonic on $U$;
3. $t \mapsto w(R_t)$ is continuous on $U$.

Lean: `GlobalTheory.CompanionTheory.Relay.log_det_eigen_frame_plurisubharmonic` (also `GlobalTheory.T.log_det_eigen_frame_plurisubharmonic`, a second name).

*Proof.* The frames show that every $R_t$ has eigenspaces of the same dimension $m$ for all $\tau$.

Part 1. The entries of the hermitian matrix of $R_t$ are smooth in $t$, and for a holomorphic frame with values in a positive hermitian space the function $\log \det \operatorname{Gram}$ is plurisubharmonic. Sum over $\tau$.

Parts 2 and 3 are local, so fix $t_0 \in U$. The cusps of small $\operatorname{nz}$ are locally finite: there are $\varepsilon > 0$ and a finite set $F$ of submodules such that, for $t$ in the ball $V$ of radius $\varepsilon$ around $t_0$ inside $U$, every $I \in F$ is a cusp of $R_t$, and every cusp $I$ of $R_t$ with $\operatorname{nz}_{R_t}(I) \leq 1$ lies in $F$. A cusp with $\operatorname{nz} > 1$ contributes a negative number to the supremum in the definition of $w$, so on $V$
$$
w(R_t) = \max\Bigl(0,\ \max_{I \in F} \bigl(-\log \operatorname{nz}_{R_t}(I)\bigr)\Bigr) .
$$
Add $\ell(t)$ inside the maximum:
$$
\ell(t) + w(R_t) = \max\Bigl(\ell(t),\ \max_{I \in F} \bigl(\ell(t) - \log \operatorname{nz}_{R_t}(I)\bigr)\Bigr) .
$$
Each term is plurisubharmonic on $V$, by part 1 and by the lemma on one cusp. The maximum of finitely many plurisubharmonic functions is plurisubharmonic, which gives part 2 on $V$. Each $\operatorname{nz}_{R_t}(I)$ is continuous and positive on $V$ by the lemma, so $w(R_t)$ is a finite maximum of continuous functions on $V$, which gives part 3. $\square$

**Remark 10.4.4 (Formalization).** The plurisubharmonic predicate used here is the one for functions on open subsets of $\mathbb{C}^n$ with the circle mean inequality (`ReciprocityTheory/AnalyticForms/PlurisubharmonicFunctions/IsPshLocallyIntegrableStatement.lean:13`), not the one for potentials on an atlas used in Section 5. Both second names only restate their theorems (`Development/AutomorphicSpectrum/Proofs/MetricProofs/LogDetCuspFramePlurisubharmonicStatement.lean` and `LogDetEigenFramePlurisubharmonicStatement.lean`). The lemma is proved in `LogDetCuspFramePlurisubharmonic.lean` (line 195) with `GlobalTheory.T.isotropic_sublattice_covolume_positive`, `GlobalTheory.T.gram_det_pos_iff_linearIndependent`, `GlobalTheory.T.isotropic_eigencomponent_conjugate_form` and two local lemmas for the quotient. The theorem is proved in `LogDetEigenFramePlurisubharmonic.lean` (line 93) with `GlobalTheory.CompanionTheory.Relay.holomorphic_family_smooth_entries` for part 1, `GlobalTheory.T.cusp_submodules_locally_finite` for the finite set $F$, the local lemma `cuspW_eq` (line 63) for the finite maximum, and `ReciprocityTheory.AnForm.A.isPsh_sup_thm` for the maximum. I did not unfold the local quotient lemmas, so the description of the quotient frame in the proof of the lemma follows their names and their use. In the definition of $\operatorname{nz}$ the family of generators is chosen by the axiom of choice; the lemma on covolumes shows that every admissible family gives the same value, which is why one family $v$ works for all $t$.
