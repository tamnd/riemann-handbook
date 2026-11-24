---
title: The modulus of an isotropic flag
decls:
  - GlobalTheory.T.isotropicFlag_levi_conj_haar_modulus
  - GlobalTheory.FlagModulus.modulus
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The modulus of an isotropic flag

This section computes how conjugation by an element of the Levi subgroup of an isotropic flag in $U(p, q)$ scales the gauge measure on the unipotent radical. The answer is a product of powers of the sizes of the Levi element on the layers of the flag, the same product that appears in the density of the flag integration formula. The result is used by the step [every character of the literature](/step/every-character-of-literature/). It is a real computation with no arithmetic input.

### Isotropic flags and their radicals

Let $n \ge 1$ and let $\varepsilon : \{1, \dots, n\} \to \{\pm\}$ be a signature, with Hermitian form $\langle x, y\rangle_J = x^* J y$ for $J = \operatorname{diag}(\varepsilon)$ and unitary group $G = U(J)$. Let $a \ge 0$ and let $j_1, \dots, j_a \ge 1$.

**Definition 2.30.1 (Isotropic flag).** An *isotropic flag* of type $(j_1, \dots, j_a)$ is a chain $W_0 \subseteq W_1 \subseteq \dots \subseteq W_a$ of complex subspaces of $\mathbb{C}^n$ with $W_0 = 0$, $\dim W_i = \dim W_{i-1} + j_i$, and $W_a$ totally isotropic for $\langle\,,\rangle_J$. Put $|j| = j_1 + \dots + j_a$.

Lean: `GlobalTheory.FlagMeas.IsIsoFlag`.

**Definition 2.30.2 (Radical and Levi of the flag).** The *unipotent radical* $N_W$ is the set of $g \in G$ with $(g - 1) W_i \subseteq W_{i-1}$ for $1 \le i \le a$ and $(g - 1) W_a^{\perp} \subseteq W_a$, where $\perp$ is taken for $\langle\,,\rangle_J$. The *Levi subgroup* $M_W$ is the set of $m \in G$ such that $m$ and its conjugate transpose $m^*$ both preserve each $W_i$.

Lean: `GlobalTheory.FlagMeas.flagN` (also `GlobalTheory.FlagMeas.flagM`, the Levi subgroup).

Since $m^* = J m^{-1} J$ for $m \in G$, the condition on $m^*$ says that $m$ preserves $J W_i$ as well. The spaces $J W_i$ are isotropic, and $M_W$ is the Levi subgroup of the parabolic of the flag that is stable under the Cartan involution.

The real dimension of $N_W$ is
$$\dim_{\mathbb{R}} N_W = 4 \sum_{i < k} j_i j_k + 2\,|j|\,(n - 2|j|) + \sum_i j_i^2.$$
The three terms count the blocks between two different layers (a $\mathfrak{gl}$-block and a block in the skew part, each of real dimension $2 j_i j_k$), the blocks between a layer and the anisotropic middle $W_a^\perp / W_a$, and the skew-Hermitian diagonal blocks.

**Definition 2.30.3 (Gauge measure on a subset).** Let $S \subseteq G$ and $d \ge 0$. A measure $\mu$ on $G$ is a *gauge measure on $S$ of dimension $d$* if $\mu$ is carried by $S$, left translation by every $s \in S$ preserves $\mu$, and
$$\lim_{r \to 0^+} \frac{\mu\{g : \|g - 1\|_{\mathrm{HS}} \le r\}}{r^d} = \operatorname{vol}(B_d),$$
the volume of the unit ball in $\mathbb{R}^d$.

Lean: `GlobalTheory.FlagMeas.IsGaugeSub`.

The normalization fixes the Haar measure of $N_W$ by its behaviour at the identity: it is the measure that the Hilbert-Schmidt metric induces on the tangent space at $1$, transported by translation.

**Definition 2.30.4 (Layer sizes and the layer product).** For $m \in M_W$ the *size* of $m$ on the $i$-th layer is
$$\tau_i(m) = \Bigl(\frac{|\det(m|_{W_i})|}{|\det(m|_{W_{i-1}})|}\Bigr)^{-1/j_i}.$$
For $\tau = (\tau_1, \dots, \tau_a)$, a real function $\Gamma$ and an integer $f \ge 1$, the *layer product* is
$$\Pi_f(\tau; \Gamma) = \prod_{i < k} \Gamma(\tau_i/\tau_k)^{2 j_i j_k f}\, \Gamma(\tau_i \tau_k)^{2 j_i j_k f} \cdot \prod_i \Gamma(\tau_i)^{2 j_i (n - 2|j|) f}\, \Gamma(\tau_i^2)^{j_i^2 f}.$$

Lean: `GlobalTheory.FlagMeas.locSize` (also `GlobalTheory.Count.layerProd`, the layer product).

### The modulus

**Theorem 2.30.5 (Conjugation modulus of the Levi on the flag radical).** Let $W$ be an isotropic flag of type $(j_1, \dots, j_a)$ with all $j_i \ge 1$, and let $\mu$ be a gauge measure on $N_W$ of dimension $\dim_{\mathbb{R}} N_W$. Then for every $m \in M_W$ the image of $\mu$ under $u \mapsto m u m^{-1}$ is
$$\mu \circ (u \mapsto m u m^{-1})^{-1} = \Pi_1(\tau(m); \mathrm{id})\,\mu.$$

Lean: `GlobalTheory.FlagModulus.modulus` (also `GlobalTheory.T.isotropicFlag_levi_conj_haar_modulus`, a second name).

*Proof.* The radical $N_W$ is a closed subgroup of $G$ and $M_W$ is a closed subgroup that normalizes it; in particular $m^{-1} \in M_W$ and $g \in N_W$ exactly when $m g m^{-1} \in N_W$. Extend the flag to the *doubled flag*
$$V_s = W_s \ (0 \le s \le a), \qquad V_s = V_{2a+1-s}^{\perp} \ (a < s \le 2a + 1),$$
which runs from $V_0 = 0$ to $V_{2a+1} = \mathbb{C}^n$ and satisfies $V_{2a+1-s} = V_s^\perp$ for all $s$. An element $g \in G$ lies in $N_W$ exactly when $g - 1$ maps each $V_{s+1}$ into $V_s$; the conditions for $s > a$ follow from those for $s \le a$ by duality. So the Lie algebra $\mathfrak{n}_W$ is the space of $X \in \mathfrak{g}$ that are strictly lower for the doubled flag. Products of such matrices stay strictly lower.

Choose a real basis $E_1, \dots, E_d$ of $\mathfrak{n}_W$ that is orthonormal for $\operatorname{Re} \operatorname{tr}(X Y^*)$. The real dimension $d$ equals $\dim_{\mathbb{R}} N_W$ above, by a count of the strictly lower part of the doubled flag inside the skew part of $\mathfrak{gl}_n$. Conjugation by $m$ preserves $\mathfrak{n}_W$, so $m E_k m^{-1} = \sum_i L_{ik} E_i$ for a real matrix $L$. The determinant of conjugation on the strictly lower part of a flag preserved by $m$ is
$$|\det L| = \prod_{s=0}^{2a} \bigl(\text{power of } |\det(m|_{V_s})| \text{ given by the dimensions}\bigr),$$
and every factor is positive. Since $m$ is unitary for $J$, $|\det m| = 1$, and for the doubled flag
$$|\det(m|_{V_{2a+1-s}})| = |\det(m|_{V_s})|, \qquad 0 \le s \le a.$$
With these relations, an identity for the doubled flag rewrites the sum of the dimensions as $\dim_{\mathbb{R}} N_W$ and the product of the determinants as $\Pi_1(\tau(m); \mathrm{id})^{-1}$. A general lemma on gauge measures says that conjugation by a linear map $L$ of the Lie algebra changes a gauge measure by $|\det L|^{-1}$. Hence the factor is $|\det L|^{-1} = \Pi_1(\tau(m); \mathrm{id})$. $\square$

**Example 2.30.6.** Let $a = 1$ and $j_1 = 1$, so $W_1$ is an isotropic line in $U(p, q)$ with $p, q \ge 1$. Then $\dim_{\mathbb{R}} N_W = 2(n - 2) + 1$, the Heisenberg group of dimension $2n - 3$. If $m$ acts on $W_1$ by a scalar $t$, then $\tau_1 = |t|^{-1}$ and the factor is $\tau_1^{2(n-2)} \tau_1^{2} = |t|^{-(2n-2)}$. This is the inverse of the usual modulus $|t|^{2n-2}$ of the parabolic subgroup of $U(p, q)$ that stabilizes an isotropic line, as it must be for the image measure.

The formula is the standard computation of the modular character of a parabolic subgroup $P = M N$, $\delta_P(m) = |\det \operatorname{Ad}(m)|_{\mathfrak{n}}|$; see Knapp, *Lie Groups Beyond an Introduction*, Ch. VIII. The point here is the explicit normalization of $\mu$ by the Hilbert-Schmidt metric.

**Remark 2.30.7 (Formalization).** The definitions `IsIsoFlag`, `flagN`, `flagM`, `detOn`, `locSize`, `dimN` and `IsGaugeSub` are in [DefClassNum.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/DefClassNum.lean#L52), and `layerProd` is in [LayerProd.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/LayerProd.lean#L32). The theorem is in [IsotropicFlagLeviConjHaarModulus.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/IsotropicFlagLeviConjHaarModulus.lean#L260); the doubled flag is `dblFlag` at line 103 and its duality is `dblFlag_sub` and `dblFlag_dual`. The main lemmas are `flagN_subgroup_closed_keeps`, `levi_compact_subgroups`, `exists_orthonormal_basis_re_trace_mul_conjTranspose`, `finrank_and_det_of_real_basis_skew_part`, `flagNilradical_finrank_and_abs_det_conj`, `signedFormOrthogonal_finrank_det_unitary`, `doubledFlag_sum_eq_unipotentDim_and_layerProd` and `map_conj_gaugeMeasure_eq_inv_det_smul`; the exponent formula in the display for $|\det L|$ is not reproduced here. The size uses `detOn`, the norm of the complex determinant of the restriction, which is $0$ for a matrix that does not preserve the subspace. The dimension `dimN` and the layer product use natural subtraction $n - 2|j|$; for an isotropic flag $2|j| \le n$, so this is harmless. The gauge condition `IsGaugeSub` asks for invariance under left translation by elements of $S$ only, and states the ball limit with `Real.sqrt` of `hs (uMat g - 1)`. The description of $M_W$ through the spaces $J W_i$, the block count of $\dim_{\mathbb{R}} N_W$, the example and the comparison with the usual modulus are ours.
