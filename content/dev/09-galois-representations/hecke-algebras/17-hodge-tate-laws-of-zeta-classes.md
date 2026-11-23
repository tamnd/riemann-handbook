---
title: Hodge-Tate laws of zeta classes
decls:
  - GlobalTheory.LambdaValuationPowers.LocGlue.localGlue
  - GlobalTheory.HTLawZeta.law_of_inputs
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hodge-Tate laws of zeta classes

On the inertia group at $\ell$, a zeta class is a multiple of the cyclotomic logarithm plus a coboundary. This section proves two results on that multiple. The first says that it is determined by a Kummer presentation of the class by polynomials in a root of unity: it is the logarithmic derivative of the polynomials at the root. The second puts this together with the coefficient law and with the existence of presentations, and gives [the Hodge-Tate law for smoothed zeta classes](/entry/k5-top/). That law goes into [the unramified zeta theorem](/entry/zeta-ur/) through [its second form](/entry/smoothed-zeta-class-hodge-tate-law/).

### Setting

Fix an odd prime $\ell$, an algebraic closure $\Omega$ of $\mathbb{Q}$, and a valuation ring $A$ of $\Omega$ with $\ell$ in its maximal ideal. Let $I_A \subseteq D_A$ be its inertia and decomposition groups in $G_{\mathbb{Q}} = \mathrm{Gal}(\Omega/\mathbb{Q})$. Let $j : \Omega \to \overline{\mathbb{Q}}_\ell$ be a ring map with $A = \{x : |j(x)| \leq 1\}$. Let $\chi : G_{\mathbb{Q}} \to \mathbb{Z}_\ell^\times$ be the [[cyclotomic character|XSGB5K2KEG]], $\chi_m$ its reduction modulo $\ell^m$, and $H_m = I_A \cap \ker\chi_m$. Let $R_0$ be the ring of elements of $A$ fixed by $I_A$. Fix a coefficient datum, with ring $\mathcal{O} \subseteq \overline{\mathbb{Q}}_\ell$ (the integers of a finite extension of $\mathbb{Q}_\ell$). For $x, x' \in \overline{\mathbb{Q}}_\ell$ write $x \equiv_n x'$ if $|x - x'| \leq |\ell^n|$. A *system* is a family of maps $Z_r : G_{\mathbb{Q}} \times (\mathbb{Z}/\ell^r)^\times \to \overline{\mathbb{Q}}_\ell$, for $r \geq 0$.

**Definition 6.17.1 (Cyclotomic logarithm at level $m$).** For $s \in G_{\mathbb{Q}}$ put $\lambda_m(s) = (\chi(s) - 1)/\ell^m$.

For $s, t \in H_m$ the value $\lambda_m(s)$ lies in $\mathbb{Z}_\ell$, and $\chi(st) - 1 = (\chi(s) - 1) + (\chi(t) - 1) + (\chi(s) - 1)(\chi(t) - 1)$ gives $\lambda_m(st) \equiv_m \lambda_m(s) + \lambda_m(t)$. So $\lambda_m$ is a homomorphism $H_m \to \mathbb{Z}/\ell^m$. It is the finite level form of $\log\chi$.

**Definition 6.17.2 (Unramified over $\mathcal{O}$).** An element $o \in \overline{\mathbb{Q}}_\ell$ is *unramified over $\mathcal{O}$* if $\sigma(o) = o$ for every $\sigma \in \mathrm{Aut}(\overline{\mathbb{Q}}_\ell/\mathbb{Q}_\ell)$ that fixes $\mathcal{O}$ pointwise and satisfies $|\sigma(x) - x| < 1$ for all $|x| \leq 1$.

The second condition says that $\sigma$ lies in the inertia group. So $o$ lies in the maximal unramified extension of the fraction field of $\mathcal{O}$. Each element of $\mathcal{O}$ is unramified over $\mathcal{O}$.

**Definition 6.17.3 (Hodge-Tate law on inertia).** Let $Z$ be a system, $m, c_0 \geq 0$, $y \in (\mathbb{Z}/\ell^m)^\times$ and $h \in \overline{\mathbb{Q}}_\ell$. Then $Z$ *satisfies the Hodge-Tate law at $(m, c_0, y)$ with value $h$* if there are $o_1, \ldots, o_q \in \overline{\mathbb{Q}}_\ell$ with $|o_i| \leq 1$, each unramified over $\mathcal{O}$, and $w_1, \ldots, w_q \in A$, such that for all $s \in H_m$
$$
\ell^{c_0} Z_m(s, y) \equiv_m \ell^{c_0} h\,\lambda_m(s) + \sum_{i=1}^q o_i\bigl(j(s w_i) - j(w_i)\bigr).
$$

The sum is an integral coboundary on $H_m$. So, up to the factor $\ell^{c_0}$ and a coboundary, $Z_m(\cdot, y)$ is $h$ times the cyclotomic logarithm on $H_m$. By the second lemma below, $h$ is then determined up to a bounded power of $\ell$.

**Definition 6.17.4 (Polynomial presentation).** Let $Z$ be a system, $m \geq c_0 \geq 0$, and $\zeta$ a primitive $\ell^m$-th root of unity. Put $n = m - c_0$ and $\zeta' = \zeta^{\ell^{c_0}}$, a primitive $\ell^n$-th root of unity. Polynomials $P_1, \ldots, P_k$ over $R_0$ and weights $o_1, \ldots, o_k \in \mathcal{O}$ form a *presentation of $Z$ at $(m, c_0, \zeta)$* if each $P_i(\zeta)$ is a unit of $A$, $|o_i| \leq 1$, and for each $s \in H_m$ there are $k_i \in \mathbb{Z}/\ell^n$ and $v_i \in \Omega$ with
$$
v_i^{\ell^n} = P_i(\zeta), \qquad s(v_i) = \zeta'^{k_i} v_i, \qquad Z_m(s, 1) \equiv_n \sum_i o_i k_i.
$$

So $k_i$ is the Kummer character of the unit $P_i(\zeta)$ at $s$, and $Z_m(\cdot, 1)$ is, modulo $\ell^n$, the combination of these Kummer characters with the weights $o_i$. This is the Kummer presentation of the chapter on [Coleman power series](/entry/p-locu/), with polynomials in $\zeta$ as units. Only the value at $y = 1$ enters.

**Definition 6.17.5 (Hodge-Tate value).** For a presentation $(\zeta, P, o)$ and $b \in \mathbb{Z}$ put
$$
\mathrm{htv}(\zeta, P, o; b) = \sum_i o_i\, j\Bigl(\frac{\zeta^b P_i'(\zeta^b)}{P_i(\zeta^b)}\Bigr).
$$

This is the logarithmic derivative $X\,\frac{d}{dX}\log P_i$ at $X = \zeta^b$, pushed to $\overline{\mathbb{Q}}_\ell$ by $j$ and weighted by $o_i$.

**Definition 6.17.6 (Hodge-Tate law of a system).** Let $m_0, c_0 \geq 0$ and let $R$ assign to each $m$, each [[Dirichlet character|JR4QSEFXWF]] $\psi$ modulo $\ell^m$ and each $z \in \overline{\mathbb{Q}}_\ell$ a value $R(m, \psi, z)$. A system $Z$ *satisfies the Hodge-Tate law with $(m_0, c_0)$ and right side $R$* if there are primitive $\ell^m$-th roots of unity $\zeta_m$ with $\zeta_{m+1}^\ell = \zeta_m$ such that for each $m \geq m_0$ there is a presentation $(P, o)$ of $Z$ at $(m, c_0, \zeta_m)$ with
$$
\sum_{b \in (\mathbb{Z}/\ell^m)^\times} \psi(b)\,\mathrm{htv}(\zeta_m, P, o; b) \equiv_{m - c_0} R\bigl(m, \psi, j(\zeta_m)\bigr)
$$
for every primitive character $\psi$ modulo $\ell^m$.

### Two local inputs

We use two local results. The first is an explicit reciprocity law for units that are polynomials in a root of unity. For explicit formulas of this kind, see Fesenko and Vostokov, *Local Fields and Their Extensions*, Chapter VII.

**Lemma 6.17.7 (Explicit reciprocity for polynomials in $\zeta$).** There is $c \geq 0$, depending only on $\ell$, with the following property. Let $\zeta$ be a primitive $\ell^m$-th root of unity, $\zeta'$ with $\zeta'^{\ell^m} = \zeta$, and $P$ a polynomial over $R_0$ with $P(\zeta)$ a nonzero unit of $A$. Let $\tau \in I_A$ and $b \in (\mathbb{Z}/\ell^m)^\times$ with $\chi_m(\tau) = b^{-1}$. Then $\zeta^b P'(\zeta^b)/P(\zeta^b) \in A$, and there is $x \in A$ such that for all $s \in H_m$ and $k, t \in \mathbb{Z}/\ell^m$: if some $v$ has $v^{\ell^m} = P(\zeta)$ and $\tau s\tau^{-1}(v) = \zeta^k v$, and $s(\zeta') = \zeta^t\zeta'$, then
$$
\ell^c k \equiv \ell^c\, t\,\frac{\zeta^b P'(\zeta^b)}{P(\zeta^b)} + s(x) - x \pmod{\ell^m A}.
$$

Here $t \equiv \lambda_m(s)$ modulo $\ell^m$. So the lemma says that the Kummer character of $P(\zeta)$ at $\tau s \tau^{-1}$ is the logarithmic derivative at $\zeta^b$ times the cyclotomic logarithm, up to a coboundary and a bounded power of $\ell$.

The second is the finite level form of a theorem of Tate: the logarithm of the cyclotomic character is not a coboundary with values in $\mathbb{C}_\ell$. See J. Tate, *p-divisible groups*, §3.

**Lemma 6.17.8 (The cyclotomic logarithm is not a coboundary).** There is $c_2 \geq 0$ with the following property. Let $m \geq 0$, $D \in \overline{\mathbb{Q}}_\ell$, $o_1, \ldots, o_q \in \overline{\mathbb{Q}}_\ell$ with $|o_i| \leq 1$ and unramified over $\mathcal{O}$, and $w_1, \ldots, w_q \in A$. If
$$
D\,\lambda_m(s) \equiv_m \sum_i o_i\bigl(j(s w_i) - j(w_i)\bigr)
$$
for all $s \in H_m$, then $D \equiv_{m - c_2} 0$.

### Uniqueness of the Hodge-Tate value

**Theorem 6.17.9 (Uniqueness of the Hodge-Tate value).** There is $c_1 \geq 0$ with the following property. Let $\nu : G_{\mathbb{Q}} \to \overline{\mathbb{Q}}_\ell^\times$, let $Z$ be a system, and let $m, c_0$ with $c_0 + c_1 \leq m$. Assume that $\nu = 1$ on $I_A$ and that
$$
Z_m(st, x) = Z_m(s, x) + \nu(s)\,Z_m\bigl(t, x\,\chi_m(s)^{-1}\bigr)
$$
for all $s, t \in D_A$ and $x \in (\mathbb{Z}/\ell^m)^\times$. Let $(\zeta, P, o)$ be a presentation of $Z$ at $(m, c_0, \zeta)$, and let $h : (\mathbb{Z}/\ell^m)^\times \to \overline{\mathbb{Q}}_\ell$ be such that $Z$ satisfies the Hodge-Tate law at $(m, c_0, y)$ with value $h(y)$ for every $y$. Then for every $y$, with $b \in \{0, \ldots, \ell^m - 1\}$ the representative of $y$,
$$
\mathrm{htv}(\zeta, P, o; b) \equiv_{m - c_0 - c_1} h(y).
$$

Lean: `GlobalTheory.LambdaValuationPowers.LocGlue.localGlue`.

*Proof.* First we compute $Z_m(\cdot, y)$ on $H_m$ from the presentation. There is $c$, depending only on $\ell$, such that for each $y$ there are $x_i \in A$ with
$$
\ell^c Z_m(s, y) \equiv_{m - c_0} \ell^c\,\mathrm{htv}(\zeta, P, o; b)\,\lambda_m(s) + \sum_i o_i\bigl(j(s x_i) - j(x_i)\bigr) \qquad (s \in H_m).
$$
To see this, choose $\tau \in I_A$ with $\chi_m(\tau) = y^{-1}$. Since $\nu = 1$ on $I_A$ and $\chi_m(s) = 1$, the cocycle relation gives $Z_m(\tau s\tau^{-1}, 1) = Z_m(s, y)$. The presentation writes $Z_m(\tau s \tau^{-1}, 1)$ as $\sum_i o_i k_i$, with $k_i$ the Kummer characters of $P_i(\zeta)$ at $\tau s\tau^{-1}$. The explicit reciprocity lemma, applied to each $P_i$ with this $\tau$ and $b$, turns $\ell^c k_i$ into $\ell^c \lambda_m(s)$ times the logarithmic derivative at $\zeta^b$ plus a coboundary $s(x_i) - x_i$. Apply $j$ and sum with the weights $o_i$.

Now fix $y$ and write $H = \mathrm{htv}(\zeta, P, o; b)$. The Hodge-Tate law gives $o'_i$ and $w'_i$ with $\ell^{c_0}Z_m(s, y) \equiv_m \ell^{c_0}h(y)\lambda_m(s) + \sum_i o'_i(j(sw'_i) - j(w'_i))$. Multiply this congruence by $\ell^c$, and the congruence above by $\ell^{c_0}$; both then hold modulo $\ell^m$. Subtract them:
$$
\begin{aligned}
\ell^{c + c_0}\bigl(h(y) - H\bigr)\lambda_m(s) \equiv_m{}& \sum_i \ell^c o'_i\bigl(j(sw'_i) - j(w'_i)\bigr) \\
&- \sum_i \ell^{c_0} o_i\bigl(j(sx_i) - j(x_i)\bigr).
\end{aligned}
$$
The weights $\ell^c o'_i$ and $-\ell^{c_0}o_i$ have absolute value at most $1$ and are unramified over $\mathcal{O}$, since $o_i \in \mathcal{O}$. The lemma on the cyclotomic logarithm gives $\ell^{c + c_0}(h(y) - H) \equiv_{m - c_2} 0$. Put $c_1 = c + c_2$. Since $c_0 + c_1 \leq m$, we can divide by $\ell^{c + c_0}$ and get $H \equiv_{m - c_0 - c_1} h(y)$. $\square$

So the Hodge-Tate value of a system is the logarithmic derivative of any presentation, up to a bounded loss of precision.

### The law for smoothed zeta classes

The data of the next theorem are those of [the Hodge-Tate law for smoothed zeta classes](/entry/k5-top/). We list them and do not repeat the conditions on them, which are stated there:

- an odd prime $\ell$, an isomorphism $\overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, $e \geq 1$, a finite set $S$ of places, $A$, a representation $W$ of newform type and a newform $g$ of weight $2e + 1$ that is a source of $W$, unramified at $\ell$;
- a tower of modular functions $X$ whose $j$-function is holomorphic on $\mathcal{H}$, a projection $\mathrm{pr}$, an integer $N$, weights $c_x \in \mathcal{O}$ for $x \in \mathbb{Z}/N$, integers $c, d$, matrices $\mathrm{gm}$, a character $\psi_0$, a coefficient datum and a unit $\alpha$, all admissible;
- the map $j$, an exponent $c_0$, and a system $Y_r : G_{\mathbb{Q}} \times (\mathbb{Z}/\ell^r)^\times \to \overline{\mathbb{Q}}_\ell^2$ that is a weighted zeta system with exponent $c_0$, a cocycle for the twist $\rho$ of $W$ and $\chi_r^{-1}$, locally constant, with integral second coordinate;
- a character $\chi_d$ modulo $N$ with values in $\mathbb{Z}_\ell$ and a linear form $\lambda$ on sequences with the congruence property of that theorem;
- an integer $d_0 \geq 2$ prime to $\ell$.

The *smoothed system* is $Z_r(s, y) = Y_r(s, y)_1 - d_0\,Y_r(s, y d_0)_1$.

**Theorem 6.17.10 (The Hodge-Tate law from its inputs).** Assume the following two statements, for all data as above.

1. (Coefficient law.) The conclusion of [the coefficient law](/entry/hco/): there are $c'$, $\kappa_0 \neq 0$ and units $p(n)$ with $p(n + 1) \equiv_n p(n)$ such that, for each index $x$ with admissible data and each zeta system $Y$ for $x$ with exponent $c_0$, $Y(\cdot)_1$ satisfies the Hodge-Tate law at $(m, c', y)$ with value $p(m)^{-1}\ell^{c_0}\kappa_0\sum_{\delta}\chi_d(\delta)^{-1}\lambda(\ell^m j(Q_\delta))$, for all $m \geq 1$, $y$, and $\beta, t$ with $\beta \equiv y \bmod \ell^m$, $\beta \equiv 1 \bmod N$ and $\ell^m t \equiv 1 \bmod N$. Here $Q_\delta$ is the Eisenstein-type series of that theorem. It is assumed in the generality stated there, with the hypothesis that each $s \in I_A$ with $\chi_1(s) = 1$ has second row $(0, 1)$ under $\rho$.
2. (Presentations.) There are $m_0, c'_0$ such that for each $m \geq m_0$ and each primitive $\ell^m$-th root of unity $\zeta$ the smoothed system has a presentation at $(m, c'_0, \zeta)$.

Then there are $m_0, c_1 \geq 0$, $\kappa \neq 0$ and $v_m \in \overline{\mathbb{Q}}_\ell$ with $|v_m| = 1$ and $v_{m+1} \equiv_m v_m$, such that the smoothed system satisfies the Hodge-Tate law with $(m_0, c_1)$ and right side
$$
\begin{aligned}
R(m, \psi, z) = {}& \bigl(1 - d_0\psi^{-1}(d_0)\bigr)\,v_m\,\kappa\,\Bigl(\sum_{a \in \mathbb{Z}/\ell^m}\psi(a)z^a\Bigr)\,\psi^{-1}(N) \\
&\cdot \lambda\Bigl(i \mapsto \sum_{x \in \mathbb{Z}/N} c_x\,E_{m,\psi,x}(\ell^m i)\Bigr).
\end{aligned}
$$
Here $E_{m, \psi, x}(i) = \sum_{\delta \in (\mathbb{Z}/N)^\times}\chi_d(\delta)\,e_{m,\psi}(x\delta, \delta; i)$, with $e_{m,\psi}$ the coefficients of the twisted Eisenstein series of the same theorem.

Lean: `GlobalTheory.HTLawZeta.law_of_inputs`.

At $z = j(\zeta_m)$ the sum over $a$ is a Gauss sum of $\psi$. The conclusion is the statement of [the Hodge-Tate law for smoothed zeta classes](/entry/k5-top/), and that theorem is this one applied to its two inputs.

*Proof.* First we get the coefficient law for each piece. If $c_x = 0$ for all $x$, then $Y(\cdot)_1 = \sum_x c_x Y_x(\cdot)_1 = 0$, and the facts below hold trivially with $\nu = 1$ and $\kappa_0 = 1$. Otherwise pick $x_0$ with $c_{x_0} \neq 0$. The admissible data at $x_0$ give the shape of $\rho$ on $D_A$: its second row is $(0, \nu(s))$, with a character $\nu$ that is $1$ on $I_A$. This is the hypothesis of the coefficient law, and it also shows that $Y(\cdot)_1$ satisfies the cocycle relation of the uniqueness theorem with this $\nu$. The coefficient law then applies to each $x$ with $c_x \neq 0$.

Next we smooth. By the Chinese remainder theorem choose $\gamma \equiv d_0 \bmod \ell^m$ with $\gamma \equiv 1 \bmod N$. Two Hodge-Tate laws at $y$ and at $y d_0$ subtract to a law for $Z$ at $y$ with value $h(y) - d_0 h(yd_0)$. In the twisted sum $\sum_b \psi(b)(h(b) - d_0h(bd_0))$, the substitution $b \mapsto b d_0^{-1}$ gives the factor $1 - d_0\psi^{-1}(d_0)$. The sum of $\psi(b)$ times the Eisenstein values over $b$ is a character sum: it equals $-N^{1 - 2e}$ times the Gauss sum $\sum_a \psi(a) j(\zeta_m)^a$, times $\psi^{-1}(N)$, times $\lambda$ of the $\chi_d$-average $E_{m,\psi,x}$ read at $\ell^m i$.

Finally, the theorem on uniqueness of the Hodge-Tate value, applied to $Z$ with this $\nu$, the presentation of input 2 and the value $h$, replaces $h(y)$ by $\mathrm{htv}(\zeta_m, P, o; b)$ modulo $\ell^{m - c'_0 - c_1}$. Summing against $\psi$ and summing over $x$ with the weights $c_x$ gives the Hodge-Tate law with the stated right side; the constant $\kappa$ and the units $v_m$ collect $\kappa_0$, $-N^{1-2e}$ and the units $p(m)^{-1}$. $\square$

**Remark 6.17.11 (Formalization).** The first theorem is proved from `GlobalTheory.LambdaValuationPowers.LocGlue.htv_coeff` (the computation in the first paragraph of the proof) and `GlobalTheory.LambdaValuationPowers.LocGlue.uniq_fix` (Tate's lemma), in [KumValSubMem.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/KumValSubMem.lean#L186). The first uses the explicit reciprocity lemma `GlobalTheory.RecConj.recip_conj`, which comes from `GlobalTheory.T.kummerCochain_eq_dlog_explicitReciprocity`, a wrapper of `GlobalTheory.RecOne.kummer_eq_dlog_one`; these are not in this chapter, and we read them as statements. The hypothesis that $A$ lies over $\ell$ is not used in the proof of Tate's lemma. A presentation constrains $Z$ only at $y = 1$ ([KumValUnique.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/KumValUnique.lean#L16)); the other values come from the cocycle relation. The second theorem ([SumTranslate.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/SumTranslate.lean#L121)) takes the coefficient law and the presentation theorem as hypotheses, in the forms of `UpperTheory.V.Z.Kato.K5.hco` and of the presentation lemma `exists_pres_smoothed`. The last step of its proof is `law_of_parts`, and the character sums are `sum_chiVal` and `sum_translate`. We have not unfolded the Eisenstein coefficients $e_{m,\psi}$ (the definition `coPtSb`) or the admissibility conditions.
