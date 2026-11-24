---
title: The local nongeneric bound
decls:
  - GlobalTheory.T.amplitude_le_mass_secondType_family
  - GlobalTheory.HL.AmpCancel.amp_le_mass
  - GlobalTheory.T.hermitianDoubleCoset_secondType_family_ampSq_le
  - GlobalTheory.HL.FamilyBound.family_bound
  - GlobalTheory.HL.NonzeroDefect.ampSq_nonzero_defect
  - GlobalTheory.T.hermitianDoubleCoset_amplitude_bound_local
  - GlobalTheory.HL.AbstractBound.ngAt
  - GlobalTheory.local_nongeneric_bound_record_family
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local nongeneric bound

At a finite place, the local factor of the double coset sum is a weighted mean square of oscillating sums over the terms of a pair of Hermitian frames. This section proves the local bound: the mean square is at most a power of the local height times the total mass, and the part that comes from terms with a nonzero defect has the extra saving $q^{-(k - 2r - 5)}$. The proof uses the [symmetric kernel](/entry/exists-symm-invariant-kernel/) of the last section for the cancellation in one family of second type terms, then adds the families, absorbs the constants, and finally passes from coordinates to an arbitrary Hermitian space. The bound is used in the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/).

We keep the [local frames setting](/entry/shares/) of the last section: the frames record $S$, the residue field size $q$, the exponent $a$, the terms $\Lambda$ of a datum $d$ with mass $\mu(\Lambda)$, phase $\omega(\Lambda)$ and defect index $\beta(\Lambda)$, and the families $\mathcal{F}(\beta, J, \beta_J)$ of second type terms. Put $\varepsilon = q^{2r + 4 - k}$.

**Definition 2.20.1 (Amplitudes, masses and the height).** For a datum $d$ and a property $P$ of lattices, the *amplitude* and the *mass* are the sums over the $N_0$-orbits of terms of $d$ with $P$,
$$a(d, P) = \sum_{[\Lambda]} \mu(\Lambda)\, \omega(\Lambda), \qquad m(d, P) = \sum_{[\Lambda]} \mu(\Lambda) \in [0, \infty].$$
Each orbit of data under the unitary group of $M_E^\perp$ has a weight $\nu(d)$, the inverse volume of its stabilizer relative to a fixed compact subgroup. For a family $P_d$ of properties put
$$\Sigma(P) = \sum_{[d]} \nu(d)\, |a(d, P_d)|^2, \qquad n_S = \sum_{[d]} \nu(d)\, m(d, \text{all}).$$
The *height* of $S$ is
$$H_S = q^{\, v(\theta) + a + v_D}, \qquad v_D = \sum_{l \ge 1,\ D_l \ne 0} v_E\big(D_l \overline{D_l}\big).$$
A term has *defect zero* if $\beta(\Lambda) = 1$, that is, if its defect lattice is all of $\Lambda \cap M_E$.

### Cancellation in one family

**Proposition 2.20.2 (Amplitude and mass of one family).** Let $k \ge 4r + 7$. For all $\beta, J, \beta_J \in \mathbb{N}$ and every datum $d$, with $P = \mathcal{F}(\beta, J, \beta_J)$,
$$|a(d, P)| \le 7\, \varepsilon\, m(d, P).$$

Lean: `GlobalTheory.HL.AmpCancel.amp_le_mass` (also `GlobalTheory.T.amplitude_le_mass_secondType_family`, a second name).

*Proof.* There are finitely many orbits of terms in $P$, by the mass bound for double cosets. First let $1 \le J \le r$, and write $J = j + 1$ with $j < r$. The [Theorem 2.19.6](/entry/exists-symm-invariant-kernel/) on symmetric kernels gives an $N_0$-invariant symmetric kernel $K \ge 0$ on $P$ with
$$\Big| \sum_y K(x, y) - 1 \Big| \le e, \qquad \Big| \sum_y K(x, y)\, \omega(y) \Big| \le e, \qquad e = \tfrac{24}{7}\, \varepsilon.$$
Write
$$\sum_x \mu(x)\omega(x) = \sum_x \mu(x) \sum_y K(x, y)\omega(y) - \sum_x \mu(x)\omega(x) \Big(\sum_y K(x, y) - 1\Big).$$
This identity needs the equality of $\sum_x \mu(x)\, \omega(x) \sum_y K(x, y)$ and $\sum_x \mu(x) \sum_y K(x, y)\, \omega(y)$, which is an exchange of $x$ and $y$ in a double sum over orbits. The exchange is allowed because $K$ is symmetric and invariant under $N_0$, because $N_0$ keeps $P$ and the phase, and because $\mu$ is constant on orbits and is an index of stabilizers. In the first sum on the right, each twisted row sum has absolute value at most $e$, so the sum is at most $e\, m(d, P)$. Since $|\omega| = 1$, the second sum is at most $e\, m(d, P)$ by the bound on the row sums. So $|a(d, P)| \le 2e\, m(d, P) = \tfrac{48}{7}\varepsilon\, m(d, P) \le 7\varepsilon\, m(d, P)$.

If $J > r$, no term lies in $P$, since a second type term has all levels at most $r$. If $J = 0$, all levels are $0$, and then the defect lattice is all of $\Lambda \cap M_E$, so the defect is zero; this is excluded for second type terms. In both cases $a(d, P) = 0$. $\square$

**Theorem 2.20.3 (Mean square of one family).** Let $k \ge 4r + 7$. For all $\beta, J, \beta_J$,
$$\Sigma\big(\mathcal{F}(\beta, J, \beta_J)\big) \le 98\, H_S^{9(r+1)^2 + 12(r+1)} \cdot 4 H_S^{4(r+1)} \cdot \varepsilon^2 \cdot n_S.$$

Lean: `GlobalTheory.HL.FamilyBound.family_bound` (also `GlobalTheory.T.hermitianDoubleCoset_secondType_family_ampSq_le`, a second name).

*Proof.* If the family has no term, the left side is $0$. Otherwise fix a term in it. Its defect index is a power $\beta = q^i$, and it is not $1$, so $q \ge 2$. Put $A_0 = H_S^{9(r+1)^2 + 12(r+1)}$ and $A_1 = 4 H_S^{4(r+1)}$.

For a datum $d$ and a term $\Lambda$ in the family, a quotient lattice attached to $\Lambda$ has order $q^m$ with $q^m \le \beta$, so $m \le i$. The terms whose quotient has order $q^m$ have mass at most $A_0 (q^m)^{k-1}$. Summing the geometric series with ratio $q^{k-1} \ge 2$,
$$m\big(d, \mathcal{F}\big) \le \sum_{m=0}^{i} A_0\, (q^{k-1})^m \le 2 A_0\, \beta^{k-1}.$$
By the [Proposition 2.20.2](/entry/amp-le-mass/), $|a(d, \mathcal{F})| \le 7\varepsilon\, m(d, \mathcal{F})$, so
$$|a(d, \mathcal{F})|^2 \le (7\varepsilon)^2 \cdot 2 A_0 \beta^{k-1} \cdot m(d, \mathcal{F}).$$
Multiply by $\nu(d)$ and sum over the data. The family lies in the set of terms of defect index $\beta$, and the weighted mass of this set is at most $A_1 \beta^{-(k-1)}\, n_S$. So
$$\Sigma(\mathcal{F}) \le 49 \varepsilon^2 \cdot 2 A_0 \beta^{k-1} \cdot A_1 \beta^{-(k-1)}\, n_S = 98\, A_0 A_1 \varepsilon^2\, n_S. \qquad \square$$

The factors $\beta^{k-1}$ and $\beta^{-(k-1)}$ cancel, so the bound does not depend on the family.

### Terms with a nonzero defect

**Theorem 2.20.4 (Nonzero defect).** Let $k \ge 4r + 7$. Then
$$\Sigma(\text{defect} \ne 0) \le H_S^{39(r+1)^2}\, q^{-(k - 2r - 5)}\, n_S.$$

Lean: `GlobalTheory.HL.NonzeroDefect.ampSq_nonzero_defect`.

*Proof.* If no term has a nonzero defect, the left side is $0$. Otherwise $q \ge 2$, and a term with a nonzero defect gives $q \le H_S$, so $H_S \ge 2$. A Cauchy-Schwarz argument over the types of terms gives
$$\Sigma(\text{defect} \ne 0) \le H_S^{2(r+2)}\, B$$
for every $B$ that bounds the mean square of each first type class (with given defect $\beta$) and of each second type family $\mathcal{F}(\beta, J, \beta_J)$. Take
$$B = 98\, H_S^{9(r+1)^2 + 12(r+1)} \cdot 4 H_S^{4(r+1)} \cdot q^{-(k - 2r - 5)}\, n_S.$$
The first type bound is $8 H_S^{9(r+1)^2 + 16(r+1)} q^{-(k-1)} n_S$, which is at most $B$ because $k - 1 \ge k - 2r - 5$. The [Theorem 2.20.3](/entry/family-bound/) on one family gives the bound with $\varepsilon^2 = q^{-2(k - 2r - 4)}$, which is at most $B$ because $2(k - 2r - 4) \ge k - 2r - 5$. Finally $392 \le 2^9 \le H_S^9$, and
$$9 + 2(r+2) + 9(r+1)^2 + 16(r+1) \le 39 (r+1)^2,$$
so $H_S^{2(r+2)} \cdot 392\, H_S^{9(r+1)^2 + 16(r+1)} \le H_S^{39(r+1)^2}$. $\square$

### The bound for a pair of Hermitian frames

Now let $M$ be a local model: a nonarchimedean local field $F$ of characteristic $0$, a reduced quadratic algebra $E$, a Haar measure and an optional splitting, with $\theta_M = 1$ if $M$ is not split and $\theta_M = \varpi$ if it is. Let $H$ be a nondegenerate Hermitian $E$-space of dimension $k + 2r + 1$, and let $P = (A, B)$ be a pair of frames in $H$ that is *related* for $\theta_M$: the spans of the frames meet in $0$, $D_{r+1}$ is a unit and every $D_l$ is $0$ or a unit, $G_P \ne 0$, the characters of the two frames agree on $N_A \cap N_B$, and the parameters satisfy fixed conditions. Let $H_P$ be its height. The pair is *prime to the place* if $M$ is not split and $G_P$ and all $D_l$ are units.

For a set $R$ of representatives of the data and of the terms modulo $N_A \cap N_B$, and a base datum $d_0$, let $\Sigma_R(T)$ be the weighted mean square of the amplitudes of the terms with property $T$, with weights $w(d_0, d)$, and let $n_R$ be the weighted total mass. A term is *nonbasic* if its lattice meets the $E$-span of its frame vectors outside their $\mathcal{O}$-span.

**Theorem 2.20.5 (Local nongeneric bound).** Let $C \ge 39$, $k \ge 4r + 7$, let $M$ be a local model, $H$ a Hermitian space of dimension $k + 2r + 1$, and $P$ a related pair of frames. Then for all $R$ and $d_0$:

1. $\Sigma_R(\text{nonbasic}) \le H_P^{C(r+1)^2}\, q^{-(k - 2r - 5)}\, n_R$;
2. $\Sigma_R(\text{basic}) \le H_P^{C(r+1)^2}\, n_R$ and $\Sigma_R(\text{all}) \le H_P^{C(r+1)^2}\, n_R$;
3. if $P$ is prime to the place, then $H_P = 1$ and $\Sigma_R(\text{basic}) = \Sigma_R(\text{all}) = n_R$.

Lean: `GlobalTheory.HL.AbstractBound.ngAt` (also `GlobalTheory.T.hermitianDoubleCoset_amplitude_bound_local`, a second name).

*Proof.* Choose coordinates: an isometry $H \cong E^{k + 2r + 1}$ carries $P$ to a frames record $S$. There is one constant $\kappa \ge 0$ such that $\Sigma_R(\text{nonbasic})$, $\Sigma_R(\text{basic})$, $\Sigma_R(\text{all})$ and $n_R$ are $\kappa$ times $\Sigma(\text{defect} \ne 0)$, $\Sigma(\text{defect zero})$, $\Sigma(\text{all})$ and $n_S$; nonbasic terms correspond to terms with a nonzero defect. The heights and the residue field sizes agree: $H_P = H_S$.

For (1), apply the [Theorem 2.20.4](/entry/amp-sq-nonzero-defect/) on nonzero defect. For (2), a bound without cancellation gives $\Sigma(\text{defect zero}) \le H_S^{39(r+1)^2} n_S$ and $\Sigma(\text{all}) \le H_S^{39(r+1)^2} n_S$. To pass from the exponent $39$ to $C$, note that if a term exists then $H_S \ge 1$, so $H_S^{39(r+1)^2} \le H_S^{C(r+1)^2}$; if no term exists then $n_S = 0$ and both sides are $0$. For (3), at a place prime to $P$ the height is $1$, every term has defect zero, and the sum over all terms equals the mass. So the sum over the terms of defect zero is the same sum. $\square$

**Corollary 2.20.6 (Local bounds for the records).** Let $C \ge 39$. Then the local nongeneric bound with constant $C$ holds for all $k, r$ with $k \ge 4r + 7$, for every datum of the seventh kind, and for every member of every family used in the global records.

Lean: `GlobalTheory.local_nongeneric_bound_record_family`.

*Proof.* The bound for $(k, r)$ is the [Theorem 2.20.5](/entry/ng-at/), with its arguments in a different order. The bounds named for a datum and for a family unfold to this bound at the $(k, r)$ of the datum, or of each member of the family. $\square$

**Remark 2.20.7 (Formalization).** The local bound is the proposition `NGAt`, with `RelG`, `PrimeTo` and the weights `Datum.wt` in [IsTermOver.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/IsTermOver.lean#L202); the conditions of `RelG` on the parameters are not unfolded here. The coordinate objects are in [ComplementReferenceCompactSubgroup.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/ComplementReferenceCompactSubgroup.lean#L154). The hypothesis $C \ge 39$ is used only to raise the exponent. In the Corollary, the second item states the same proposition three times: `NonGenericLocalBoundOfLargeRank` and `adm5` both unfold to `Conclusion1` ([LocalNongenericBoundRecordFamily.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LocalNongenericBoundRecordFamily.lean#L19)). The Proposition gives the constant $48/7$, which is weakened to $7$. The family bound gets $q \ge 2$ from a term of the family, although $q \ge 2$ holds for every frames record. The word "nongeneric" is only a name; no file explains it.
