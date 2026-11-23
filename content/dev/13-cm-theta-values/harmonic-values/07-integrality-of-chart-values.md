---
title: Integrality of chart values
decls:
  - ReciprocityTheory.ChartRestriction.G.TB.WickVanishing.Closed.symmetric_canonical_gauge
  - ReciprocityTheory.ChartRestriction.G.TB.WickVanishing.Closed.scaled_connection_columns
  - ReciprocityTheory.ChartRestriction.G.PullbackSections.Pf.chartValJ
  - GlobalTheory.PlaceInt.HostChart.chBound_host
  - ReciprocityTheory.ChartRestriction.G.Out.TLinPf.tLin_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Integrality of chart values

The [previous section](/entry/sum-hv-formal-kernel/) bounds a sum of harmonic values from below by a chart bound $(e, \rho)$. This section proves the chart bound at a finite place. The value of $\rho$ is explicit: it is $0$ at the places where the [[discriminant|E0VZTNPJXA]] of the CM field is a unit, and it is a multiple of the valuation of the discriminant at the other places. The proof has three layers. First, an algebraic statement on formal power series: iterated canonical connections, applied to an integral series and paired with a harmonic polynomial, give values in a power of an ideal. Second, a version of this statement for columns of sections, which is the form of a chart value. Third, the chart bound at all places. The last part of the section proves a tangent linearity statement for Mumford uniformizations, which the step [every character](/step/every-character/) uses next to these results. The background is in [formal group laws](/learn/formal-groups/#formal-group-laws), [the logarithm](/learn/formal-groups/#the-invariant-derivation-and-the-logarithm), [semi-abelian degenerations](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction) and [$p$-adic numbers and local fields](/learn/number-fields/#p-adic-numbers-and-local-fields).

### Connections on formal series

Let $R \subset k$ be a subring of a field such that every $y \in k$ has a multiple $Ny \in R$ with $N > 0$ an integer. Let $J \subset k$ be an $R$-submodule with $1 \in J$. Let $B$ be a formal group datum of dimension $d$ over $R$ with an action of $\mathcal{O}$, let $h$ be a canonical gauge with logarithmic part $h_L$, and let $m$ be an integer. We work with power series in two sets of variables $X = (X_1, \dots, X_d)$ and $Y = (Y_1, \dots, Y_d)$. Let $\sigma_1, \dots, \sigma_d$ be the coordinate series of the gauge.

**Definition 2.7.1 (connection operator).** Let $u, \varphi \in R^d$. The *connection operator* of the pair $\xi = (u, \varphi - \sigma_1 u)$ acts on a series $G(X, Y)$ by
$$\nabla_\xi G = D_u G + \sum_i (D_u \sigma_i)\, \partial_{Y_i} G + \sum_i \varphi_i\, \partial_{Y_i} G - m \Big(\sum_i (Y_i - \sigma_i) u_i\Big) G,$$
where $D_u$ is the derivative in the direction $u$ in the variables $X$. We call the set of such pairs $\xi$ the *horizontal set* $H$.

**Definition 2.7.2 (pairing).** For two pairs $\xi = (\xi_1, \xi_2)$ and $\eta = (\eta_1, \eta_2)$ in $k^d \times k^d$, put
$$\beta_H(\xi, \eta) = \sum_i (\eta_{2,i}\, \xi_{1,i} - \xi_{2,i}\, \eta_{1,i}).$$

Three identities hold for these operators. Conjugation of $\nabla_\xi$ by $\exp(\pm m h_L)$ keeps integral series integral, for $\xi \in H$. The commutator is a scalar: $[\nabla_\xi, \nabla_\eta] = m\, \beta_H(\xi, \eta)$. And for $\varphi \in R^d$, the operator $\nabla_{(0, \varphi)}$ kills every series in $X$ alone. These are the analogues, on the formal group, of the Heisenberg relations of the [Fock model](/learn/theta/#the-fock-model): $\nabla_\xi$ acts as a creation or annihilation operator, and $\beta_H$ is the symplectic form.

Now fix a finite set of *letters* $l$. Each letter has a colour $c_l$ and a side $s_l \in \{0, 1\}$. Each letter carries a pair $\xi(l) \in H$ and a vector $\psi(l) \in J^d$. For a multi-index $n$ on the letters, let $\mathrm{pm}(n)$ be the sum over the colours $q$ of the minimum of the degree of $n$ on the letters of colour $q$ and side $0$ and its degree on those of colour $q$ and side $1$. Let $\nabla^n$ be the iterated operator that applies $\nabla_{\xi(l) + (0, \psi(l))}^{n_l}$ first for the letters of side $0$ and then for those of side $1$. For a polynomial $P = \sum_n P_n\, n$ in the letters, put $P(\nabla) = \sum_n P_n \nabla^n$.

**Theorem 2.7.3 (symmetric canonical gauge).** Assume that $\beta_H(A_l, A'_{l'}) = 0$ unless $c_l = c_{l'}$ and $s_l \neq s_{l'}$, for each of the three choices $(A, A') = (\xi, \xi)$, $((0, \psi), \xi)$ and $(\xi, (0, \psi))$. Let $P$ be a polynomial in the letters with coefficients in $R$ such that $\mathrm{pm}(n) \le e$ for every monomial $n$ of $P$. Let $f$ be an integral series in $X$. Then the constant coefficient of $P(\nabla)\big(\exp(m h_L) f\big)$ lies in $J^e$.
Lean: `ReciprocityTheory.ChartRestriction.G.TB.WickVanishing.Closed.symmetric_canonical_gauge`

*Proof.* Put $E_0 = \exp(m h_L)$. It is a unit with constant term $1$, and its inverse is $\exp(-m h_L)$. Call a series *good* if it has the form $E_0 g$ with $g$ integral. By the first identity, every $\nabla_\xi$ with $\xi \in H$ maps good series to good series. The constant coefficient of a good series lies in $R$.

Split each letter operator as $\nabla_{\xi(l)}$ plus the operator of $(0, \psi(l))$. By the hypothesis, $\beta_H$ vanishes on two letters of the same side, so by the commutator identity the operators of one side commute. Move each operator of $(0, \psi)$ to the right. By the kill identity it gives zero when it reaches the series in $X$. On its way it meets operators $\nabla_{\xi(l)}$, and each exchange produces the scalar
$$\kappa_{l, l'} = m\, \beta_H\big(\xi(l), (0, \psi(l'))\big).$$
This is a Wick expansion. Let $\Delta_\kappa = \sum_{l, l'} \kappa_{l, l'}\, \partial_l \partial_{l'}$ be the second order operator on polynomials in the letters. Then
$$P(\nabla)(E_0 f) = \sum_{t \ge 0} \mathrm{ev}\Big(\frac{\Delta_\kappa^t}{t!} P\Big)(E_0 f),$$
where $\mathrm{ev}$ applies the operators $\nabla_{\xi(l)}$ in the order of the sides. By the hypothesis, $\kappa_{l, l'} \neq 0$ only if $l$ and $l'$ have the same colour, $l$ has side $1$ and $l'$ has side $0$. Each entry of $\kappa$ lies in $J$, because $\psi(l') \in J^d$ and the first component of $\xi(l)$ lies in $R^d$.

Fix $t$. If $t \le e$, the divided power $\Delta_\kappa^t P / t!$ has coefficients in $J^t$, because the entries of $\kappa$ lie in $J$ and $P$ has coefficients in $R$. Since $1 \in J$, we have $J^t \subset J^e$. The evaluation then acts on the good series $E_0 f$, so the constant coefficient lies in $J^e$. If $t > e$, then $\Delta_\kappa^t P = 0$. Indeed, each application of $\Delta_\kappa$ removes one letter of side $1$ and one letter of side $0$ of the same colour, so it lowers $\mathrm{pm}$ by exactly $1$ on every monomial. Since $\mathrm{pm} \ge 0$, and $\mathrm{pm} \le e$ on $P$, the iterate of order $t$ vanishes. Sum over $t$. $\square$

### Columns

A chart value is a product over columns $b = 1, \dots, n$. Each column has its own series $f_b$ and its own monomial. The next statement is the column form of the theorem.

**Theorem 2.7.4 (scaled connection columns).** Keep the setting and the hypotheses on $\beta_H$. Let $P = \sum_{\mathrm{mo}} P_{\mathrm{mo}}\, \mathrm{mo}$ be a polynomial with coefficients in $R$ in the column letters. For each monomial $\mathrm{mo}$ and column $b$, let $\mathrm{col}(\mathrm{mo}, b)$ be the part of $\mathrm{mo}$ in column $b$, and assume $\sum_b \mathrm{pm}(\mathrm{col}(\mathrm{mo}, b)) \le e$. Let $f_1, \dots, f_n$ be integral. Then
$$\sum_{\mathrm{mo}} P_{\mathrm{mo}} \prod_{b=1}^n \mathrm{cc}\Big(\nabla^{\mathrm{col}(\mathrm{mo}, b)}\big(\exp(m h_L) f_b\big)\Big) \in J^e,$$
where $\mathrm{cc}$ is the constant coefficient.
Lean: `ReciprocityTheory.ChartRestriction.G.TB.WickVanishing.Closed.scaled_connection_columns`

*Proof.* Fix $\mathrm{mo}$ and put $e_b = \mathrm{pm}(\mathrm{col}(\mathrm{mo}, b))$. Apply the symmetric canonical gauge theorem to the single monomial $\mathrm{col}(\mathrm{mo}, b)$ with bound $e_b$. The factor of column $b$ lies in $J^{e_b}$. The product lies in $J^{\sum_b e_b}$, and this is contained in $J^e$ because $1 \in J$ gives $J^{a} \subset J^{a'}$ for $a \ge a'$. Multiply by $P_{\mathrm{mo}} \in R$ and sum. $\square$

### Chart values with a defect ideal

We now pass from the formal statement to chart values. Let $R$, $k$ and $J$ be as above. The letters are now pairs $(\tau, i)$ with $\tau$ in a finite type and $i$ a coordinate index. The types carry an involution $\tau \mapsto \bar\tau$, a colour and a side, such that $\bar\tau$ has the colour of $\tau$ and the opposite side. A letter carries a direction $u$, a shift $\varphi$ and a defect $\psi \in J^d$, as before.

**Theorem 2.7.5 (chart values with defect).** Assume that the directions are orthogonal for the pairing of the chart whenever two letters have types $\tau'$ and $\tau$ with $\tau' \neq \bar\tau$, and assume the three compatibility conditions between $u$, $\varphi$ and $\psi$ that the chart data give. Let $P$ be a harmonic polynomial with coefficients in $R$ such that $\sum_b \mathrm{pm}(\mathrm{col}(\mathrm{mo}, b)) \le e$ for every monomial $\mathrm{mo}$ of $P$. Let $f_1, \dots, f_n$ be integral series. Then
$$\sum_{\mathrm{mo}} P_{\mathrm{mo}} \prod_{b=1}^n \nabla(f_b, u)(\mathrm{col}(\mathrm{mo}, b)) \in J^e.$$
Lean: `ReciprocityTheory.ChartRestriction.G.PullbackSections.Pf.chartValJ`

*Proof.* The orthogonality hypothesis is the vanishing of $\beta_H$ on pairs $(\xi, \xi)$ of letters with wrong types. The three compatibility conditions give the vanishing of $\beta_H$ on the pairs with $(0, \psi)$. Because $P$ is harmonic, the second order operator of the chart vanishes on $P$ after the renaming of the letters to types. With this vanishing, the column form of the identity of the [third section](/entry/harm-nab-eq-poly-deriv/) rewrites each value $\nabla(f_b, u)(\mathrm{col})$ as the constant coefficient of the iterated connection applied to $\exp(m h_L) f_b$. Then the theorem on scaled connection columns gives the result. $\square$

When $J = R$ the statement says that chart values of integral series under integral harmonic polynomials are integral. The ideal $J$ measures the failure of the chart data to be integral. At a ramified place the defect $\psi$ is not integral, but a fixed power of a uniformizer times $\psi$ is.

### The chart bound at all places

Let $E$ be the CM field of the host data, with discriminant $d_E$ and degree $[E:\mathbb{Q}]$. Let $T$ be a complete [[discrete valuation ring|MGM3CNJW9V]] with normalized valuation $v$, and let $C$ be an integral chart at an integral framed point $y$. Let $N$ be the conductor of the host data. Every prime that divides $d_E$ divides $N$. For a prime $p$, put
$$\mathrm{vd}(p) = \frac{v_p(d_E)}{[E:\mathbb{Q}]}.$$
Let $\mathrm{DF}(w)$ be the degree bound of the harmonic polynomials of weight $w$, and let $\mathrm{DF}_w \ge \mathrm{DF}(w)$.

**Theorem 2.7.6 (chart bound at the host field).** For every $e > 0$, the chart $C$ satisfies the chart bound $(e, \rho)$ with
$$\rho = \sum_{p \mid N} \frac{v(p)}{e}\, \mathrm{vd}(p)\, \frac{\mathrm{DF}_w}{2}.$$
Lean: `GlobalTheory.PlaceInt.HostChart.chBound_host`

*Proof.* Each term of the sum is at least $0$, and the chart bound is monotone in $\rho$: a bound for $\rho$ is a bound for every $\rho' \ge \rho$. There are two cases.

Case 1: every prime $p \mid N$ is a unit in $T$. Every prime factor of $|d_E|$ divides $N$, so $d_E$ is a unit in $T$. In this case the chart data are integral, and the theorem on chart values with defect applies with $J = R$ and $\psi = 0$. The chart values of integral series under integral harmonic polynomials are integral, so the chart bound holds with $\rho = 0$. Monotonicity gives the claim.

Case 2: some prime $p \mid N$ is not a unit in $T$. Then $p$ is the residue characteristic of $T$. Write $|d_E| = p^a m$ with $p \nmid m$. The host data give two more facts: $E$ is [[Galois|0QMZAQ6QQ4]] over $\mathbb{Q}$, and complex conjugation moves every prime of $\mathcal{O}_E$ above $p$. Under these conditions the ramified chart bound holds with
$$\rho_p = \frac{v(p)}{e}\cdot \frac{a}{[E:\mathbb{Q}]}\cdot \frac{\mathrm{DF}(w)}{2}.$$
Its proof applies the theorem on chart values with defect with a fractional ideal $J$ generated by a negative power of $p$. A harmonic polynomial of degree at most $\mathrm{DF}(w)$ has $\mathrm{pm} \le \mathrm{DF}(w)/2$ on each monomial, which gives the factor $\mathrm{DF}(w)/2$. Now $a/[E:\mathbb{Q}] = \mathrm{vd}(p)$ and $\mathrm{DF}(w) \le \mathrm{DF}_w$, so $\rho_p$ is at most the term of $p$ in the sum, and that term is at most the sum. Monotonicity gives the claim. $\square$

The step [every character of literature](/step/every-character-of-literature/) uses this bound at each finite place. The sum over $p$ then becomes a multiple of $\log |\mathrm{disc}|$, which the global estimate absorbs.

### Tangent linearity

The last result is of a different kind. It does not involve harmonic values. It concerns the Mumford uniformization of a degenerating abelian scheme with an action of $\mathcal{O}$, and the step [every character](/step/every-character/) uses it to compare trivializations on first order thickenings.

**Definition 2.7.7 (global functions condition).** An abelian scheme $A \to S$ satisfies the *global functions condition* if pullback $\Gamma(S, \mathcal{O}_S) \to \Gamma(A, \mathcal{O}_A)$ is bijective.

**Theorem 2.7.8 (tangent linearity).** Assume the global functions condition for all abelian schemes. Let $A$ be an abelian scheme over $S$ with an $\mathcal{O}$-linear Mumford uniformization, and let $t_e$ be the trivialization of the line bundle at the unit section. Let $a \in \mathcal{O}$ and let $\chi$ be a character of the torus. Then the trivialization $t_e(\bar a \chi)$, times the pullback of the unit $u$ of the uniformization, corresponds to the pullback of $t_e(\chi)$ along the action of $a$ on the first order thickening of the unit section.
Lean: `ReciprocityTheory.ChartRestriction.G.Out.TLinPf.tLin_of`

*Proof.* The two trivializations of the same line bundle on the thickening differ by a unit $\rho$. The unit $\rho$ is invariant under the translations of the uniformization, because both trivializations are. So $\rho$ descends to a unit $v$ on the abelian scheme. By the global functions condition, $v$ is the pullback of a constant $\kappa$ on the base. Evaluate at the unit section. Both trivializations restrict to the same trivialization of the fibre at $e$, so $\kappa = 1$. Hence $\rho = 1$, and restriction to the thickening gives the correspondence. $\square$

The global functions condition is classical. Over a field, it says that a complete connected variety has only constant functions. Over a general base, each fibre has only constant functions, so cohomology and base change gives $\pi_* \mathcal{O}_A = \mathcal{O}_S$; see Mumford, *Abelian Varieties*, Section 5.

**Remark 2.7.9 (Formalization).** The symmetric canonical gauge theorem is in [Closed.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/TaylorDiscriminants/WickVanishing/Closed.lean#L25). It applies the conditional form in [SCMain.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/TaylorDiscriminants/WickVanishing/SCMain.lean#L28) to the three identities of [ConnectionKillsSeries.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/TaylorDiscriminants/ConnectionKillsSeries.lean). The statement is in [GermSC.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/TaylorDiscriminants/GermSC.lean#L29). The column form is in the same file [Closed.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/TaylorDiscriminants/WickVanishing/Closed.lean#L47). It proves the product step again with a private helper. A second declaration with the same short name, in [SCCols.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/TaylorDiscriminants/WickVanishing/SCCols.lean#L35), takes the three identities as hypotheses and derives the column form from the single-column form. The chart value theorem is in [ChartValJ.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/PullbackSections/HolomorphicFamilies/ChartValJ.lean#L31) and needs a raised heartbeat limit. Its orthogonality hypothesis is used verbatim as the first vanishing condition. The chart bound is in [HarmonicValuationLowerBoundHostFieldAllPlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/HarmonicValuationLowerBoundHostFieldAllPlaces.lean#L36). Tangent linearity is in [ESecStruct.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/ChartPullbacks/TangentLinearity/ESecStruct.lean#L31), with the statement in [UnifBaseChangeSt.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/UnifBaseChangeSt.lean#L122). It takes the global functions condition of [GlobalSectionsRankAlgClosed.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/GlobalSectionsRankAlgClosed.lean#L150) as a hypothesis, although that condition is proved in [GlobalFnsHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/AbelianSchemeLawProofs/GlobalFnsHolds.lean#L16).
