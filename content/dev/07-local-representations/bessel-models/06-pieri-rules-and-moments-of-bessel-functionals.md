---
title: Pieri rules and moments of Bessel functionals
decls:
  - Gp91.GlobalTheory.bessel_ev_projector_value
  - Gp91.GlobalTheory.T.dual_tensor_bessel_moment
  - Gp91.GlobalTheory.DualStepBound.dual_step_bound
  - Gp91.GlobalTheory.T.lowering_scalar_sq_mul_degree_ratio_le
  - Gp91.GlobalTheory.MomentStep.moment_step
  - Gp91.GlobalTheory.T.family_setup_cayley_moment
  - Gp91.GlobalTheory.Moment.moment_first_length
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Pieri rules and moments of Bessel functionals

This section compares the Bessel functionals of two discrete series whose Harish-Chandra parameters differ by one unit vector. The tool is the Pieri rule: the tensor product of a discrete series with the dual of the standard representation splits into discrete series with lowered parameters. We compute the scalar by which a Pieri projector acts on a Bessel functional, bound the square of this scalar against the ratio of formal degrees, and then prove by induction a bound for the moments $\int \| g^{-1} f_0 \|^{2q} \, \| l(\sigma(g) w) \|^2 \, dg$ of a Bessel functional. These moment bounds control the growth of Bessel functions, and the product moment bounds of the uniform estimate on Bessel periods use them. We keep the notation of [the first section](/entry/bounded/) and of [the uniqueness theorem](/entry/bessel-map-uniq-gap/).

### The family and the Pieri data

Let $k \geq 1$, $n = 2r + k + 1$, and let $\varepsilon$ be the sign vector of the form $H$. A *family* is a map $\nu \mapsto R_\nu$ from $\mathbb{Z}^n$ to unitary representations of $G$ such that $R_\nu$ is a discrete series with Harish-Chandra parameter $\lambda + \nu$ whenever $|\nu|_1 \leq q_0$ ([discrete series](/learn/representations/#discrete-series)). The numerical hypotheses on $(\lambda, u, b, b_v, g_a, h, q_0)$ are these:

1. the entries of $\lambda$ differ from the entries $u_1, \dots, u_k$ by half-integers, and they interlace: $u_1 > \lambda_0 > u_2 > \lambda_1 > \dots > u_k > \lambda_{k-1}$;
2. $0 \leq \lambda_a \leq b_v/8$ for $a \leq k-2$, and $-2b_v \leq \lambda_a \leq -b_v$ for $a \geq k-1$;
3. $|\lambda_a| \leq b$ and $|u_i| \leq b$;
4. the first $k-1$ entries of $\lambda$ are at least $g_a$ apart, $\lambda$ has gap at least $h$, and $100(q_0+1) \leq \min(g_a, h)$;
5. $10^6 n^7 \leq b_v$.

So the parameter of $\pi$ interlaces with $\lambda$, as in the branching law for discrete series ([interlacing and the branching law](/learn/periods/#interlacing-and-the-branching-law-for-discrete-series)). For each $\nu$ with $|\nu|_1 \leq q_0$ we fix a Bessel functional $l_\nu$ of $R_\nu$ of type $(\psi_{\mathrm{std}}, \pi)$ with the integral identity of Bessel models, and we let $d_\nu > 0$ be the formal degree of $R_\nu$ for a fixed Haar measure.

Let $V^* = \mathbb{C}^n$ with $g$ acting by $(g^{-1})^{\mathsf T}$. On $R \otimes V^*$, written as $n$-tuples $x = (x_c)$ of vectors of $R$, the group acts by $(g \cdot x)_c = \sum_j (g^{-1})^{\mathsf T}_{cj}\, \sigma(g) x_j$. For a covector $a \in \mathbb{C}^n$ and $v \in R$ put
$$a \otimes v = (a_c v)_c, \qquad \mathrm{ev}(a)(x) = \sum_{i,j} \overline{a_i} H_{ij} x_j .$$

**Definition 6.6.1 (Pieri data).** Let $R$ be a discrete series with parameter $\mu$ and $R_s$ a discrete series with parameter $\mu - e_s$ for each $s$. *Pieri data* are maps $\iota_{s,c} : R_s \to R$ and $p_{s,c} : R \to R_s$ for $0 \leq s, c < n$, continuous on smooth vectors, such that $y \mapsto (\iota_{s,c} y)_c$ and $x \mapsto \sum_c p_{s,c}(x_c)$ are $G$-equivariant, $\sum_s \iota_{s,c} \sum_d p_{s,d}(x_d) = x_c$, $\sum_c p_{s,c} \iota_{s,c} = 1$, and $\sum_c p_{s,c} \iota_{t,c} = 0$ for $s \neq t$. *Hermitian Pieri data* have in addition signs $\epsilon_s = \pm 1$ such that, for the form $\langle x, x' \rangle = \sum_{i,j} H_{ij} \langle x_j, x'_i \rangle$, the embeddings $\iota_s$ multiply inner products by $\epsilon_s$ and have orthogonal images.

So $R \otimes V^* = \bigoplus_s R_s$, with each summand of multiplicity one. This is the Pieri rule for $\mathrm{GL}_n$ transported to discrete series by Zuckerman tensoring; see [the ingredients of Zuckerman tensoring](/entry/zuckerman-ingredients/). We write $P_s = \iota_s \circ p_s$ for the projector onto the summand $R_s$.

Let $f_0 = e_0$ if $r \geq 1$ and $f_0 = z$ if $r = 0$, and let $f_0^\flat$ be the covector $c \mapsto \langle e_c, f_0 \rangle_H$. A direct computation with $H^2 = 1$ gives $\mathrm{ev}(f_0^\flat)(x) = \sum_j (f_0)_j x_j$.

### The value of a Pieri projector

**Theorem 6.6.2 (Bessel value of a Pieri projector).** Let $R$ be a discrete series with parameter $(\varepsilon, \mu)$ and $R_s$ discrete series with parameters $(\varepsilon, \mu - e_s)$, with Pieri data. Let $z \in W_0$ with $T_z > 0$, let $\pi$ be of Harish-Chandra type with infinitesimal parameter $u$, and let $l$ be a Bessel functional of $R$ of type $(\psi_{\mathrm{std}}, \pi)$. Then for each $s$ there is $c_s \in \mathbb{C}$ with
$$|c_s| = T_z \, \frac{\prod_{i=1}^{k} |\mu_s - \tfrac12 - u_i|}{\prod_{t \neq s} |\mu_s - \mu_t|}$$
and $l\big(\mathrm{ev}(f_0^\flat)(P_s(f_0^\flat \otimes v))\big) = c_s \, l(v)$ for all smooth $v$.

Lean: `Gp91.GlobalTheory.bessel_ev_projector_value` (also `Gp91.GlobalTheory.T.dual_tensor_bessel_moment`).

*Proof.* Take a frame $g$ for $z$. It carries the coordinates of $\mathrm{U}(k)$ and of the flag into standard position. In particular $g^{-1} f_0 = \beta e_{i_0}$ and $g^{\mathsf T} f_0^\flat = \alpha e_{n-1}$, where $i_0 = 0$ and $\alpha = \beta = 1$ if $r \geq 1$, and $i_0 = n-1$, $\beta = \sqrt{T_z}$, $\alpha = -\sqrt{T_z}$ if $r = 0$.

The smooth vectors of a discrete series form a module for $\mathfrak{gl}_n(\mathbb{C})$, with $E_{ab}$ acting by the derivative along $g E_{ab} g^{-1}$. The Pieri data transport to these modules, and the transported maps are compatible with the dual tensor action on $M \otimes V^*$. The Capelli determinant acts on $R$ by a scalar fixed by $\mu$. Hence the Casimir operator $\sum_{a,b} E_{ab} E_{ba}$ acts on $R$ by $\sum_a \mu_a^2 - \sum_a \rho_a^2$, where $\rho$ is the half sum for $\mathrm{GL}_n$, and on $R_t$ by the same expression for $\mu - e_t$. The split Casimir $x \mapsto (-\sum_c E_{bc} x_c)_b$ on $M \otimes V^*$ differs from the Casimir of the tensor product by the two Casimirs of the factors. So it acts on the summand $R_t$ by a scalar that depends only on $\mu_t$, through $\mathrm{Cas}(\mu - e_t) - \mathrm{Cas}(\mu) = 1 - 2\mu_t$. The value is $\theta_t = -\mu_t + \frac{1-n}{2}$.

Since the $\theta_t$ are distinct, $P_s$ is the Lagrange polynomial $\prod_{t \neq s} (\Omega - \theta_t)/(\theta_s - \theta_t)$ in the split Casimir $\Omega$. This explains the denominator. Now apply $l$ to the entry of $P_s(x)$ in position $i_0$, with $x$ concentrated in position $n-1$. The entries $E_{ab}$ that lie in the Lie algebra of $N$ act on $l$ by the derivative of $\psi_{\mathrm{std}}$, and the entries in the block of $\mathrm{U}(k)$ act through $\pi$. The vanishing of $l$ on the remaining triangular entries reduces the value to a polynomial in $\mu_s$ whose roots are $\tfrac12 + u_i$, the infinitesimal character of $\pi$. This gives a scalar $c$ with $|c| = T_z^{\delta} \prod_i |\mu_s - \tfrac12 - u_i| / \prod_{t \neq s} |\mu_s - \mu_t|$, with $\delta = 1$ for $r \geq 1$ and $\delta = 0$ for $r = 0$.

Finally, $\mathrm{ev}(f_0^\flat)(x) = \sum_j (f_0)_j x_j = \sum_d (g^{-1} f_0)_d \sum_c g_{cd} x_c$, and only $d = i_0$ survives. So $c_s = \beta c \alpha$, and $|\alpha \beta| = T_z$ for $r = 0$ and $1$ for $r \geq 1$. In both cases $|c_s|$ has the stated value. $\square$

We have not unfolded the lemma that computes the projector entry under a linear functional, or the eigenvalue of the Capelli determinant. The explanation of the numerator through the infinitesimal character of $\pi$ describes their use, not their proofs.

### The dual step bound

Fix a family as above and $\nu$ with $|\nu|_1 + 1 \leq q_0$. Put $\mu = \lambda + \nu$.

**Theorem 6.6.3 (Dual step bound).** Let Hermitian Pieri data for $R_\nu$ and the $R_{\nu - e_s}$ be given, and assume that $l_\nu$ is not zero on smooth vectors. Let $s$ and $\kappa \in \mathbb{C}$ satisfy
$$l_{\nu - e_s}\Big( \sum_c p_{s,c}\big( (f_0^\flat)_c v \big) \Big) = \kappa \, l_\nu(v) \quad \text{for all smooth } v.$$
Then
$$|\kappa|^2 \, \frac{d_\nu}{d_{\nu - e_s}} \leq T_z \, b^4 .$$

Lean: `Gp91.GlobalTheory.DualStepBound.dual_step_bound` (also `Gp91.GlobalTheory.T.lowering_scalar_sq_mul_degree_ratio_le`).

*Proof.* By the theorem above there is $c$ with $|c| = T_z \prod_i |\mu_s - \frac12 - u_i| / \prod_{t \neq s} |\mu_s - \mu_t|$ and $l_\nu(\mathrm{ev}(f_0^\flat)(P_s(f_0^\flat \otimes v))) = c\, l_\nu(v)$.

The Hermitian structure gives an adjoint relation: $l_\nu(\mathrm{ev}(f_0^\flat)(\iota_s y)) = \epsilon_s \overline{\kappa}\, l_{\nu - e_s}(y)$ for smooth $y \in R_{\nu - e_s}$. Apply it to $y = p_s(f_0^\flat \otimes v)$ with $l_\nu(v) \neq 0$. We get $c = \epsilon_s \overline{\kappa} \kappa$, so $|\kappa|^2 = |c|$.

By Schur orthogonality and Harish-Chandra's formula, there is a constant $c_0 > 0$ with $d_{\nu'} = c_0 \, \mathrm{fd}(\lambda + \nu')$ for all $\nu'$ in the family, where
$$\mathrm{fd}(\mu) = \prod_{a < b} \frac{|\mu_a - \mu_b|}{b - a}$$
([discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees)). Only the factors with index $s$ change from $\mu$ to $\mu - e_s$, so
$$\frac{d_\nu}{d_{\nu - e_s}} = \prod_{t \neq s} \frac{|\mu_s - \mu_t|}{|\mu_s - 1 - \mu_t|} .$$
The gap hypotheses make all factors nonzero. Multiplying,
$$|\kappa|^2 \frac{d_\nu}{d_{\nu - e_s}} = T_z \, \frac{\prod_{i=1}^k |\mu_s - \tfrac12 - u_i|}{\prod_{t \neq s} |\mu_s - 1 - \mu_t|} .$$
The *lowering bound* says that the last ratio is at most $64 e \sqrt{k}\, b^3$ if $s \leq k-2$ and at most $16 e\, b^2$ otherwise. The numerical hypotheses give $b \geq b_v \geq 10^6 n^7$, so both are at most $b^4$. $\square$

The ratio bound uses the interlacing of $\mu$ with $u$ and the gaps: each factor $|\mu_s - \frac12 - u_i|$ in the numerator is paired with a factor of the denominator of comparable size. We have not unfolded the proof of this ratio bound.

### Moments

The *length* of $g \in G$ is $L(g) = \| g^{-1} f_0 \|$, the Euclidean norm. Let $\nu_q$ be the quotient measure on $R \backslash G$. A vector $w$ of $R_\nu$ is *at level $j$* if it lies in a finite-dimensional space, stable under the operators $E_{ab}$ with $\varepsilon_a = \varepsilon_b$, on which the Casimir of $K$ is at most $(\sqrt{c_K} + 4nj)^2$, where $c_K$ is the Casimir value of the lowest $K$-type, and if $w$ is a sum of weight vectors whose weights are within $\ell^1$ distance $j$ of the highest weight of the lowest $K$-type. Here the $E_{ab}$ are operators on smooth vectors that satisfy the relations of $\mathfrak{gl}_n$, attached to a fixed Cayley matrix $Q$.

**Theorem 6.6.4 (Moment step).** Let $|\nu|_1 + 1 \leq q_0$, $j \leq 4n^2$, $q \geq 0$ and $M \geq 0$. Assume that for every $s$ and every $y$ at level $j+2$ in $R_{\nu - e_s}$,
$$\int L(g)^{2q} \, d_{\nu - e_s} \| l_{\nu - e_s}(\sigma(g) y) \|^2 \, d\nu_q(g) \leq M \|y\|^2 .$$
Then for every $w$ at level $j$ in $R_\nu$,
$$\int L(g)^{2q+2} \, d_\nu \| l_\nu(\sigma(g) w) \|^2 \, d\nu_q(g) \leq n^2 \, T_z b^4 \, (6 b_v)^{2(2r+2)} \, M \, \|w\|^2 .$$

Lean: `Gp91.GlobalTheory.MomentStep.moment_step` (also `Gp91.GlobalTheory.T.family_setup_cayley_moment`).

*Proof.* If $l_\nu$ vanishes on smooth vectors, the left side is $0$. Otherwise take Hermitian Pieri data for $R_\nu$, and let $\kappa_s$ be the scalars of the dual step bound, so that $|\kappa_s|^2 d_\nu \leq T_z b^4 d_{\nu - e_s}$. Transport the Pieri data along $Q$ and put $y_{d,s} = p'_s(e_d \otimes w)$ for $0 \leq d < n$.

Two facts about the transported data enter. First, each $y_{d,s}$ is at level $j + 2$ in $R_{\nu - e_s}$, and $\sum_s \| y_{d,s} \|^2 \leq (6 b_v)^{2(2r+2)} \|w\|^2$ for each $d$. Second, for almost every $g$ there are coefficients $a_d(g)$, the pairings of $(g^{-1})^{\mathsf T} Q_d$ with $f_0^\flat$, such that
$$\sum_d |a_d(g)|^2 = L(g)^2, \qquad a_d(g) \, l_\nu(\sigma(g) w) = \sum_s \epsilon_s \overline{\kappa_s} \, l_{\nu - e_s}(\sigma(g) y_{d,s}) .$$
The first identity comes from the orthonormality of the columns of $Q$. The second is the transfer of the Bessel functional through the Pieri data, by the adjoint relation.

Now fix $g$. Write $L(g)^{2q+2} d_\nu \|l_\nu(\sigma(g)w)\|^2 = \sum_d L(g)^{2q} d_\nu \| a_d(g) l_\nu(\sigma(g) w)\|^2$. By the Cauchy-Schwarz inequality over $n$ terms and the bound on $|\kappa_s|^2$,
$$\| a_d(g) l_\nu(\sigma(g)w) \|^2 d_\nu \leq n \, T_z b^4 \sum_s d_{\nu - e_s} \| l_{\nu - e_s}(\sigma(g) y_{d,s}) \|^2 .$$
Integrate over $R \backslash G$ and apply the hypothesis to each $y_{d,s}$. This gives the bound $n T_z b^4 M \sum_{d,s} \|y_{d,s}\|^2 \leq n^2 T_z b^4 (6b_v)^{2(2r+2)} M \|w\|^2$. $\square$

**Theorem 6.6.5 (Moments of Bessel functionals).** Let $q \geq 0$, $|\nu|_1 + q \leq q_0$ and $j + 2q \leq 4n^2$. Then for each $w$ at level $j$ in $R_\nu$,
$$\int L(g)^{2q} \, d_\nu \| l_\nu(\sigma(g) w) \|^2 \, d\nu_q(g) \leq \big( n^2 \, T_z b^4 \, (6 b_v)^{2(2r+2)} \big)^q \, \|w\|^2 .$$

Lean: `Gp91.GlobalTheory.Moment.moment_first_length`.

*Proof.* Induction on $q$, for all $\nu$ and $j$ at once. For $q = 0$ the bound is $\int d_\nu \|l_\nu(\sigma(g) w)\|^2 \, d\nu_q \leq \|w\|^2$. This is the isometry property of Bessel functionals: $\sqrt{d_\nu}\, l_\nu$ is an isometry from $R_\nu$ into $L^2(R \backslash G, \pi \otimes \psi_{\mathrm{std}})$ when $l_\nu \neq 0$. For the step from $q$ to $q+1$, apply the moment step with $M = C^q$. Its hypothesis is the induction hypothesis for $\nu - e_s$ and level $j + 2$, which is allowed since $|\nu - e_s|_1 \leq |\nu|_1 + 1$ and $(j+2) + 2q \leq 4n^2$. $\square$

**Remark 6.6.6 (Formalization).** The objects `ev`, `tm` and `flat` are the contraction, the tensor with a covector and the $H$-dual covector above, and Pieri data are the structures `TensRaw` and `TensH` ([SumIoPrAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/SumIoPrAlt.lean#L77)). We have not unfolded `CapParam`, `GlRel`, `IsCayleyU`, `IsE`, `GapOK` or the Casimir value `ckv`. The three wrappers with the prefix `T.` are one-line proofs of the form `first | exact @… | …` under `maxHeartbeats 1000000` ([FamilySetupCayleyMomentStatement.lean](lean:CompanionTheory/AutomorphicTheory/PieriRules/ThetaBesselIsometries/FamilySetupCayleyMomentStatement.lean#L16)). The lemma $|\nu - e_s|_1 \leq |\nu|_1 + 1$ is proved three times, and the whole folder of these proofs has a second copy under `Development/AbelianVarietyTheory/Proofs/JetHarmonics/`, stated with other hypothesis bundles. The ratio bound comes from a lemma in [AlgebraicIdentityHigherDegree.lean](lean:Formalism/FlagUnipotentLattices/AlgebraicIdentityHigherDegree.lean#L24), whose name does not describe it. The parameter $u$ is a function on $\mathbb{N}$ of which only the values at $1, \dots, k$ are used.
