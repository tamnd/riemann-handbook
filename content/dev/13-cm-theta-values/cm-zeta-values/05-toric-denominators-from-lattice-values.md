---
title: Toric denominators from lattice values
decls:
  - GlobalTheory.JoinFun.joinOut_of_lat
  - GlobalTheory.T.toricPeriodZeta_of_latticeValue_statements
  - GlobalTheory.JoinFun.joinOut_of_jetInt
  - GlobalTheory.T.toricPeriodZetaStatements_of_jetIntegrality_algebraicity
  - GlobalTheory.JoinFun.joinOut_of_five
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Toric denominators from lattice values

This section collects the results of the chapter so far into one statement, which we call the *toric package*. It has five parts: denominators of partial zeta values, denominators of toric sums of CM lattice values, Galois transport of these values, the same for sums twisted by class group characters, and a reflection identity for Hecke $L$-functions. The package follows from five published theorems. The proof is a chain of three compositions. The last one is used by the [toric package from the literature](/entry/join-out-of-literature/).

We keep the notation of the previous sections: admissible data, the constants $a_0$, $c$ and $e$, the size $\mathcal{B}_\lambda(r)$, CM data, conjugate weights, and the normalized coordinate $\operatorname{co}_\kappa(\Omega, T) = C(\kappa)\,T/\Omega^{w(\kappa)}$.

### The fifth published input

Let $E$ be a totally complex field, $\varphi$ a CM type of $E$, and $\chi$ a unitary Hecke character of $E$ of infinity type $n \in \mathbb{Z}^I$ with respect to $\varphi$ ([infinity type and algebraic characters](/learn/class-field-theory/#infinity-type-and-algebraic-characters)). Suppose that $\chi$ has conductor exponent $a_w$ at each finite prime $w$.

**Theorem 1.5.1 (functional equation of Hecke $L$-functions; Hecke, Tate).** If $n_i \neq 0$ for some $i$, there are completed $L$-functions $\Lambda$ of $(\chi, n)$ and $\Lambda'$ of $(\chi^{-1}, -n)$ such that for all $s \in \mathbb{C}$
$$\Lambda(s) = \varepsilon_\infty(n)\, \varepsilon_f(\chi, a, s)\, \Lambda'(1 - s),$$
with the archimedean and finite root numbers $\varepsilon_\infty$ and $\varepsilon_f$.

See Neukirch, *Algebraic Number Theory*, Chapter VII, §8, and [Tate's thesis and Hecke $L$-functions](/learn/class-field-theory/#tates-thesis-and-hecke-l-functions).

### Bounds on valuations

For a prime $l$, a real $r$ and $a \in \mathbb{C}$, we say that *$a$ has $l$-adic order at least $-r$* if for all $m \in \mathbb{Z}$ and $n \geq 1$ with $r \leq m/n$ the number $l^m a^n$ is $l$-integral, that is, $N l^m a^n$ is an algebraic integer for some integer $N$ prime to $l$.

Let $\Lambda$ be the ring of integers of $\mathbb{Q}(\sqrt{-d})$, viewed as a lattice in $\mathbb{C}$. For a lattice sum value $T$ put
$$\beta_\kappa(T) = \frac{(C(\kappa)\, T)^{12}}{\Delta(\Lambda)^{w(\kappa)}}.$$
If $\Omega^{12} = \Delta(\Lambda)$ then $\beta_\kappa(T) = \operatorname{co}_\kappa(\Omega, T)^{12}$. So $\beta_\kappa$ is the twelfth power of the normalized coordinate, without a choice of root.

For admissible data with prime $l$ and weight $\kappa$ put $n_l = 0$ if $c = 0$, and otherwise
$$n_l = 2s|I|\, c + |\kappa|\bigl(2c + 1 + [l = 2] + \tfrac12[l = d]\bigr).$$
The *bound* is $b_l = 12\,(e + n_l + w(\kappa)\, a_0)$.

**Definition 1.5.2 (lattice integrality).** *Lattice integrality holds at ramified primes* if for all admissible data with prime $l$, lattice $L$ and $c \neq 0$, every $\kappa$ and every lattice sum $S$ of type $(2s, \kappa)$ for $L$, the number $\beta_\kappa(S(0))$ has $l$-adic order at least $-b_l$. *Lattice integrality holds at unramified primes* if the same holds for all data with $c = 0$.

**Definition 1.5.3 (divided power expansion).** The *divided power expansion holds* if the conclusion of the [Theorem 1.3.7](/entry/cm-lattice-divided-power-jet-integrality-of-elliptic-cm/) on CM jets holds for data with $c \neq 0$, with the last bound replaced by
$$\partial_u \mathcal{G}(0) \prod_{i \in I} \frac{(b_i/a_i)^{\kappa_i}}{a_i^{2s}\, \kappa_i!} \in \mathcal{B}_\lambda\bigl(e + 2s|I|\, c + |\kappa|(c + 1 + [l = 2])\bigr).$$

**Definition 1.5.4 (algebraicity of lattice values).** *Lattice values are algebraic* if for every $K$, $\iota$, $d$, $\delta$ as in the [Theorem 1.4.5](/entry/lattice-value-conjugation-of-elliptic-cm-theorems/) on Galois conjugation, every $\Omega_0$ with $\Omega_0^{12} = \Delta(\iota\mathcal{O}_K)$, every CM datum on a CM field $E \supset K$, every $\kappa$, $y$ and every lattice sum $S$ of type $(2s, \kappa)$ for $L(\mathfrak{c}, y)$, the number $\operatorname{co}_\kappa(\Omega_0, S(0))$ is algebraic.

### The toric package

Let $F$ be totally real of degree $g$ and $k \geq 1$. For $n \geq 1$ let $m_l(n)$ be the least value of $v_l(a^n - 1)$ over integers $a \geq 2$ prime to $l$. For $z : \operatorname{Cl}(F) \to \mathbb{Q}$ let $e_l(z) = \max_C \max(0, -v_l(z(C)/2^g))$.

**Definition 1.5.5 (zeta denominators).** The *zeta denominators* hold for $F$ in weight $k$ if there is $z : \operatorname{Cl}(F) \to \mathbb{Q}$ such that each $z(C)$ is the value at $1 - k$ of a partial zeta function of $C$, and if every such $z$ satisfies:

1. for every prime $l$, $e_l(z) \leq g\, v_l(2) + m_l(gk)$;
2. for $l \neq 2$, $m_l(gk) = 0$ if $(l - 1) \nmid gk$, and $m_l(gk) = 1 + v_l(gk)$ if $(l - 1) \mid gk$;
3. $m_2(gk) = 2 + v_2(gk)$;
4. if $gk \geq 16$, then $e_l(z) = 0$ for almost all $l$ and $\sum_l e_l(z) \log l \leq gk \log(gk + 1)$.

The *toric package* is the conjunction of five statements.

1. *Zeta denominators*: they hold for the real subfield of every CM field in every weight $2s$, $s \geq 1$.
2. *Toric denominators*: for every abelian CM field $E$ with field data $(d, \varphi)$ and $s \geq 1$ there are zeta values $z$ of weight $2s$ such that the following holds. For every $\kappa$, every admissible $\mathfrak{f}$ and every Hecke character $\chi$ of type $(s, \kappa)$ for $(\mathfrak{f}, \emptyset)$, every prime $l$ and every $Q$ admissible for $\mathfrak{f}$ with no prime over $l$: the numbers $\beta_\kappa(\lambda_f(\chi, s, y)^{-1} S(0))$, for lattice sums $S$ of type $(2s,\kappa)$ for $L(\mathfrak{c}, y)$, and $\beta_\kappa(T)$, for the toric sums $T = \sum_q \lambda_f(\chi\psi, s, y_q)^{-1} S_q(0)$ over $q \in \operatorname{Pic}(\mathcal{O}_{\mathfrak{c}})$, with $\psi$ a Hecke character trivial at infinity and on $\widehat{\mathcal{O}}_{\mathfrak{c}}^\times$, have $l$-adic order at least $-b_l$.
3. *Transport*: for $K$ imaginary quadratic of discriminant $-d$ with $d > 4$, the automorphisms of $\mathbb{C}$ fixing $K$ act on $j(\mathcal{O}_K)$ through ideals $\mathfrak{a}(\sigma)$ and ideles $t(\sigma)$, with $j(\mathfrak{a}(\sigma)) = \sigma(j(\mathcal{O}_K))$. An equidistribution condition holds for the ideals, and a transport law holds for lattice sums with all $\kappa_i \geq 1$.
4. *Twisted transport*: for $K$, $\iota$, $d$, $\delta$ as above there is $\Omega_0 \neq 0$ with two properties. Take a CM datum with all $\kappa_i \geq 1$, a character $\chi$ of type $(s, \kappa)$ for $(\mathfrak{f}, \emptyset)$, and a character $\psi$ of $\operatorname{Pic}(\mathcal{O}_{\mathfrak{c}})$. First, the twisted sum $T = \sum_{q} \psi(q)^{-1}\lambda_f(\chi, s, y_q)^{-1} S_q(0)$ has an algebraic coordinate $\operatorname{co}_\kappa(\Omega_0, T)$. Second, let $g$ act on $K^{ab}$ as the Artin symbol of an idele with finite part $t$. Then there is $\Omega_1 \neq 0$ such that $g(\operatorname{co}_\kappa(\Omega_0, T)) = \operatorname{co}_\kappa(\Omega_1, \|t\|^{-|\kappa|}(\lambda_f(\chi', s, t)\, g\psi([t]))^{-1} T')$. Here $\chi'$ is the conjugate character, with $\lambda_f(\chi', s, \cdot) = g \circ \lambda_f(\chi, s, \cdot)$ and infinity type $\kappa' + s$, and $T'$ is the twisted sum for $\kappa'$, $\chi'$ and $g \circ \psi$.
5. *Reflection*: an identity $\Lambda(s)\Lambda_0(1 - s) = \epsilon\, \Lambda(1 - s)\Lambda_0(s)$, with $\epsilon$ a unit away from a fixed set, between completed Hecke $L$-functions of the main argument at integers $s \leq 0$ in a range.

### The three compositions

**Theorem 1.5.6 (toric package from lattice values).** Assume the main theorem of complex multiplication, the Hilbert class field theorem, the theorems of Siegel-Klingen and Deligne-Ribet, and the functional equation of Hecke $L$-functions. If lattice integrality holds at ramified and at unramified primes, lattice values are algebraic, and the conclusion of the [Theorem 1.4.5](/entry/lattice-value-conjugation-of-elliptic-cm-theorems/) on Galois conjugation holds, then the toric package holds.

Lean: `GlobalTheory.T.toricPeriodZeta_of_latticeValue_statements` (also `GlobalTheory.JoinFun.joinOut_of_lat`, a second name).

*Proof.* We prove the five parts.

1. The zeta denominators follow from the theorems of Siegel-Klingen and Deligne-Ribet.
2. The toric denominators follow from the zeta denominators and from lattice integrality at ramified and unramified primes.
3. The transport follows from the Hilbert class field theorem, the algebraicity of lattice values and the Galois conjugation law.
4. The main theorem of complex multiplication gives, for each such $g$ and $t$, a torsion transport $(\Lambda_1, \Omega_1)$ of $(\iota\mathcal{O}_K, \Omega_0)$. With the algebraicity and the Galois conjugation law, this gives the twisted transport.
5. The functional equation of Hecke $L$-functions gives the reflection, together with the boundedness of completed Hecke $L$-functions in vertical strips and their nonvanishing in the relevant range. $\square$

**Theorem 1.5.7 (toric package from jet integrality).** Assume the five published theorems: the four above and the functional equation of partial zeta functions. If the conclusion of the [Theorem 1.3.7](/entry/cm-lattice-divided-power-jet-integrality-of-elliptic-cm/) on CM jets holds, lattice values are algebraic, and the Galois conjugation law holds, then the toric package holds.

Lean: `GlobalTheory.T.toricPeriodZetaStatements_of_jetIntegrality_algebraicity` (also `GlobalTheory.JoinFun.joinOut_of_jetInt`, a second name).

*Proof.* By the functional equation of partial zeta functions and the [Theorem 1.1.10](/entry/hecke-weight-two-of-fe/) on Hecke's series, the derivative formula and class invariance of the [Theorem 1.2.9](/entry/cm-lattice-deriv-class-invariance-of-hecke/) on derivatives hold. The jet bound implies the divided power expansion: $1/\kappa_i! \in \mathcal{B}_\lambda(\kappa_i)$, since $v_l(\kappa_i!) \leq \kappa_i$, and the exponent of the expansion has room to spare. Class invariance and the divided power expansion give lattice integrality at ramified primes. Class invariance and the jet bound give lattice integrality at unramified primes. Now apply the Theorem above. $\square$

**Theorem 1.5.8 (toric package from the literature).** Assume the main theorem of complex multiplication, the Hilbert class field theorem, the theorems of Siegel-Klingen and Deligne-Ribet, the functional equation of partial zeta functions, and the functional equation of Hecke $L$-functions. Then the toric package holds.

Lean: `GlobalTheory.JoinFun.joinOut_of_five`.

*Proof.* This is the Theorem above applied to the [Theorem 1.3.7](/entry/cm-lattice-divided-power-jet-integrality-of-elliptic-cm/) on CM jets, to the algebraicity of lattice values, and to the [Theorem 1.4.5](/entry/lattice-value-conjugation-of-elliptic-cm-theorems/) on Galois conjugation. Each of the three is proved from the published theorems. $\square$

**Remark 1.5.9 (Formalization).** The three theorems are compositions ([JoinOutOfFive.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/JoinOutOfFive.lean#L15)). The first takes four published theorems and not the functional equation of partial zeta functions; the second uses that functional equation only to get class invariance. In the first two theorems the first name is proved from the second by `first | exact @…`. The algebraicity of lattice values is proved elsewhere and has no entry in this chapter. We have not unfolded the equidistribution and the transport law in the transport part, the reflection part and its hypotheses on field data and nonvanishing, or the root numbers $\varepsilon_\infty$ and $\varepsilon_f$. We have read the statements of the lemmas in the five steps, not their proofs. The divided power expansion uses $\kappa_i!$, but the jet bound it comes from does not.
