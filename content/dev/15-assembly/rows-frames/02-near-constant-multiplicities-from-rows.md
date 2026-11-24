---
title: Near constant multiplicities from rows
decls:
  - GlobalTheory.FinGL.MultSharpObj.multSharp
  - GlobalTheory.ColumnMultSum.columnMult
  - GlobalTheory.passIn3_of_rows
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Near constant multiplicities from rows

This section proves the pass condition of the third place series from the rows of a real datum. The pass condition asks for a finite family of representations $\tau_s$ of the finite group $G$ of the family such that each character of the family occurs, a base character occurs once in each $\tau_s$, and a second level character occurs in each $\tau_s$ with a multiplicity that is near a fixed number $\bar n$. The result is used by [the pass condition at a real point](/entry/pass-in3-at-real-t-alt/), which feeds the [definite side condition](/step/definite-side-condition-def/) of [the unitary hypotheses](/proof/unitary-hypotheses/). The main work is a local count at each place: the multiplicity of a generic character of a unipotent group in a cuspidal parabolic induction. A product over the places then gives the global bound.

We use the notation of the last section. Let $E$ be a number field and $\mathrm{Pg}$ a finite set of places $P$ of $E$, with residue fields $k_P$ of size $q_P$. For $r \geq 1$ put
$$G_0 = \prod_{P \in \mathrm{Pg}} \mathrm{GL}_r(k_P).$$
A function $\chi$ on $G_0$ is a *product of cuspidal characters* if $\chi(x) = \prod_P \theta_P(x_P)$ with each $\theta_P$ a cuspidal parabolic product character of $\mathrm{GL}_r(k_P)$. A *level datum* is a subgroup $H \subseteq G_0$ with a character $\omega : H \to \mathbb{C}^\times$. The *multiplicity* of $(H, \omega)$ in $\chi$ is
$$m(H, \omega; \chi) = \frac{1}{|H|} \sum_{h \in H} \chi(h)\, \omega(h)^{-1}.$$
When $\chi$ is the character of a representation, this is the dimension of the $\omega$-eigenspace of $H$. We use [representations of a finite group](/learn/representations/#representations-of-a-group) of Volume 1.

Fix integers $\rho \geq 0$ and $k \geq 1$ with $\rho + k + 1 \leq r$. Index rows and columns by $0, \dots, r - 1$. Let $U_r(k_P)$ be the upper unitriangular group. Let $U^{\rho,k}(k_P)$ be the subgroup of $u \in U_r(k_P)$ with $u_{i, \rho + k} = 0$ for $\rho \leq i < \rho + k$. The *edges* of $(\rho, k)$ are the pairs $(i, i + 1)$ with $i + 1 \notin \{\rho, \rho + k\}$, and the pair $(\rho - 1, \rho + k)$ when $\rho \geq 1$. On $U^{\rho,k}(k_P)$ the sum of the entries at the edges is additive. So for an additive character $\psi_P$ of $k_P$ the function
$$\omega_P(u) = \psi_P\Big( \sum_{(i,j) \text{ edge}} u_{ij} \Big)$$
is a character of $U^{\rho,k}(k_P)$. Put $H^{\rho,k} = \prod_P U^{\rho,k}(k_P)$ with the product character $\omega^{\rho,k}$. For $\rho = 0$ the edges are the superdiagonal pairs other than $(k - 1, k)$, and the entry at $(k-1, k)$ is zero on $U^{0,k}$; so $\omega^{0,k}$ is the sum of the superdiagonal entries. The family $\psi = (\psi_P)$ is *generic* if each $\psi_P$ is nontrivial. Put
$$\bar n = \prod_{P \in \mathrm{Pg}} q_P^{\,k}.$$

The local input is a count of the multiplicity of $\omega_P$ in a cuspidal induction. For a block function $b$ on $\{0, \dots, r-1\}$ and $j \geq 0$ let $N_b(j)$ be the number of sets $J$ of blocks whose union has exactly $j$ elements, and put $\gamma_q(0) = 1$ and $\gamma_q(l) = q^l - q^{l-1}$ for $l \geq 1$. The local theorem says that, for a cuspidal datum $\sigma$ on $P_b$ and $q = |k_P| \geq r$,
$$m\big(U^{\rho,k}, \omega_P; \mathrm{Ind}\, \sigma\big) = \sum_{j} N_b(j)\, \gamma_q(k - j)$$
and that this sum lies between $q^k (1 - 1/q)$ and $q^k \big(1 + (2r - 1)/q\big)$.

**Theorem 7.2.1 (Sharp multiplicities).** Let $f \geq 1$, $g > 0$, $\rho \geq 0$ and $k \geq 1$, and put $r = k + 2\rho + 1$. Let $|\mathrm{Pg}| = 2f$, $4fr \leq g$ and $g \leq q_P$ for each $P \in \mathrm{Pg}$. Let $\psi$ be generic and let $\chi$ be a product of cuspidal characters on $G_0$. Then for both level data $(H^{\rho,k}, \omega^{\rho,k})$ and $(H^{0,k}, \omega^{0,k})$ there is a natural number $n$ with
$$m(H, \omega; \chi) = n, \qquad |n - \bar n| \leq \frac{8fr}{g}\, \bar n.$$

Lean: `GlobalTheory.FinGL.MultSharpObj.multSharp`.

*Proof.* Write $\chi = \prod_P \theta_P$. The group $H$ and its character are products over $P$, so the sum over $H$ splits:
$$m(H, \omega; \chi) = \prod_{P} m\big(U(k_P), \omega_P; \theta_P\big).$$
Each $\theta_P$ is the character of the induction of a cuspidal datum, and $r \leq 4fr \leq g \leq q_P$, so the local theorem applies at each $P$. In both cases $\rho' + k + 1 \leq r$, with $\rho' = \rho$ or $\rho' = 0$. So the local multiplicity is a natural number $n_P$ with
$$q_P^{\,k}\Big(1 - \frac{1}{q_P}\Big) \leq n_P \leq q_P^{\,k}\Big(1 + \frac{2r - 1}{q_P}\Big).$$
Put $n = \prod_P n_P$. Since $q_P \geq g$, the product of the lower bounds gives
$$n \geq \bar n \Big(1 - \frac{1}{g}\Big)^{2f} \geq \bar n \Big(1 - \frac{2f}{g}\Big) \geq \bar n \Big(1 - \frac{8fr}{g}\Big)$$
by Bernoulli's inequality. For the upper bound put $x = (2r - 1)/g$. Then $2fx \leq 4fr/g \leq 1$, and
$$(1 + x)^{2f} \leq e^{2fx} \leq 1 + 4fx \leq 1 + \frac{8fr}{g},$$
since $e^y \leq 1 + 2y$ for $0 \leq y \leq 1$. So $n \leq \bar n (1 + 8fr/g)$. $\square$

Now let $G$ be the finite group of a family, with an isomorphism $e : G \to G_0$, and let $(P_1, \psi_1)$ be the second level datum of a face of the family. Let $g = \min(g_1, g_2)$ for the two primes of the host. The *level ratio bound* is $4 f r \leq g$. The *level record* of the real datum says that $e(P_1)$ is the conjugate of $H^{\rho,k}$ by a permutation of the coordinates at each place, and that $\psi_1$ corresponds to $\omega^{\rho,k}$ for a generic $\psi$.

**Theorem 7.2.2 (Column multiplicities).** Assume the level record, $|\mathrm{Pg}| = 2f$, $g \leq q_P$ for all $P \in \mathrm{Pg}$ and the level ratio bound. Let $\chi$ be a character of the family such that $\chi \circ e^{-1}$ is a product of cuspidal characters. Then $m(P_1, \psi_1; \chi) = n$ for a natural number $n$ with
$$|n - \bar n| \leq \frac{8fr}{g}\, \bar n.$$

Lean: `GlobalTheory.ColumnMultSum.columnMult`.

*Proof.* A permutation of the coordinates is conjugation by a permutation matrix $w$ at each place. The rows of the datum give $k \geq 1$ and $r = k + 2\rho + 1$. The function $\chi \circ e^{-1}$ is a class function, so the multiplicity of the conjugate level datum $(w H^{\rho,k} w^{-1}, \omega^{\rho,k}(w^{-1} \cdot w))$ in it equals the multiplicity of $(H^{\rho,k}, \omega^{\rho,k})$. Transport along $e$ identifies $m(P_1, \psi_1; \chi)$ with this number. The theorem on sharp multiplicities gives the bound. $\square$

The pass condition has these parts. There are a finite set $S$, representations $\tau_s$ of $G$ for $s \in S$ and a number $\bar n > 0$ such that:

1. a rational condition on the family at the second level datum holds;
2. the family $(\tau_s)$ is good, and the characters of the $\tau_s$ are exactly the characters of the family;
3. the multiplicity of the base datum $(P_0, \psi_0)$ in each $\tau_s$ is $1$;
4. for each $s$, with $\delta$ the deviation of the family,
$$(1 - \delta)\, \bar n \leq m(P_1, \psi_1; \tau_s) \leq (1 + \delta)\, \bar n.$$

**Theorem 7.2.3 (Pass condition from rows).** Let the field of the family be totally complex. Assume the weak characterisation of the real datum, the condition $\mathrm{Ok}_3$ of the family with constant $1$, the primitive rows of the face, label maps for the series idempotents as in the last section, and the level ratio bound. Let the deviation be $\delta = 8fr/g$ and let the logarithmic size be $\log |G|$. Then the pass condition holds.

Lean: `GlobalTheory.passIn3_of_rows`.

*Proof.* The weak characterisation gives the level record and the group record. The condition $\mathrm{Ok}_3$ gives that each character of the family is absolutely irreducible. The group record, the label maps and [the theorem on good characters](/entry/irreducible-character-good-idempotent-cuspidal-product/) of the last section show that each character of the family, moved to $G_0$, is a product of cuspidal characters.

The base level datum $(P_0, \psi_0)$ has multiplicity one in each character of the family: the sum of $\chi(h)\psi_0(h)^{-1}$ over $P_0$ is $|P_0|$. A general construction then gives a good family $(\tau_s)$ whose characters are those of the family and in which $(P_0, \psi_0)$ occurs once. The group record also gives $|\mathrm{Pg}| = 2f$ and $q_P \geq g$. The rational condition comes from the row test of the primitive rows. Take $\bar n = \prod_P q_P^{\,k}$, which is positive.

For the multiplicities, fix $s$. The theorem on column multiplicities gives $n$ with $m(P_1, \psi_1; \chi_s) = n$ and $|n - \bar n| \leq \delta \bar n$, where $\chi_s$ is the character of $\tau_s$. The multiplicity of a linear character of $P_1$ in $\tau_s$ equals the character sum $m(P_1, \psi_1; \chi_s)$, and this sum is the natural number $n$ in a field of characteristic zero. So $m(P_1, \psi_1; \tau_s) = n$, and the bound is part 4. The logarithmic size is $\log |G|$ by assumption. $\square$

**Remark 7.2.4 (Formalization).** The pass condition is `PassIn3` in [PrimitivePackageFullHecke.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/PrimitivePackageFullHecke.lean#L24), with fields `CxPassIn3` in [NearConstantMultiplicities.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/NearConstantMultiplicities.lean#L17). We have not unfolded the rational field `ratMuP`; it comes from `ratMuP_of_rowTest`. The local theorem is `T.symmetricPositionCharMultiplicity_parabolicInduction` with the two sided bound `sum_numBlockSets_mul_gamma_two_sided_bounds`, packed as `placeBound`; we read their statements. The sharp theorem is the one line `multSharp_of_placeBound placeBound`. Its hypothesis $0 < g$ is used only to divide. The proof of the pass condition takes the two parts of the sharp theorem but uses only the part for $(H^{\rho,k}, \omega^{\rho,k})$; the second part is dropped with `-` in `columnMult` ([ReordEqConj.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ReordEqConj.lean#L35)). The constants `C` and `CH` of the pass condition do not enter the proof. The cuspidal product step goes through `T.goodCharacter_placewise_cuspidal_parabolic_product`, which applies the theorem on good characters of the last section.
