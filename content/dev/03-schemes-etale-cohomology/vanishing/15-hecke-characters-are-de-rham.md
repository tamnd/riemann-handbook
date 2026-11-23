---
title: Hecke characters are de Rham
decls:
  - HodgeLocalDeRhamField.HLdR.field_outright
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hecke characters are de Rham

The last result of the chapter is that the $l$-adic character of an algebraic Hecke character is de Rham at each finite place, with the single Hodge-Tate jump $-n(\iota \circ \tau)$ at each embedding $\tau$. Volume 4 proves this from two conditions on Lubin-Tate periods, the tilt condition and the product condition ([Theorem 4.8.6 of Volume 4](/entry/field-of-leaves/)). This section proves the two conditions, so the result holds with no hypotheses. The result is used in the step [EveryCharacter](/step/every-character/), where it gives de Rham Galois characters, and through a second name in the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/). For the background see [Hecke characters](/learn/class-field-theory/#hecke-characters), [period rings](/learn/galois-representations/#period-rings) ([[Fontaine's period rings|K6HW8YWCQJ]]) and [de Rham representations](/learn/padic-hodge/#de-rham-representations).

We keep the notation of Volume 4. So $l$ is a prime, $K$ is a finite extension of $\mathbb{Q}_l$ in $\bar{\mathbb{Q}}_l$, $\mathbb{C}_l$ is the completion of $\bar{\mathbb{Q}}_l$, $\mathcal{O}^\flat$ is the tilt of $\mathcal{O}_{\mathbb{C}_l}$ with $x \mapsto x^\sharp$, $[x]$ is the Teichmüller lift in $B_{\mathrm{dR}}^+$, $\theta : B_{\mathrm{dR}}^+ \to \mathbb{C}_l$ is the usual map, and $\mathrm{Fil}^k = (\ker \theta)^k$. A Lubin-Tate datum $(\pi, z)$ for $\chi : G_K \to K^\times$ is as in Definition 4.7.1, with $q = \#(O_K/\pi)$, and a pre-period is as in Definition 4.7.2 ([Theorem 4.7.4 of Volume 4](/entry/pre-period/)).

### The tilt condition

**Theorem 9.15.1 (Tilt condition).** Let $\chi : G_K \to K^\times$ be a homomorphism with a Lubin-Tate datum $(\pi, z)$, and let $\mu$ be an embedding of $K$. Then there are a ring map $r : O_K \to \mathcal{O}^\flat$ and elements $v_0, v_1, \dots$ of $\mathcal{O}^\flat$ such that:

1. $v_{n+1}^q = v_n$ for all $n$, $v_0 \neq 0$ and $|v_0^\sharp| < 1$;
2. for each $c \in O_K$ there is $c' \in O_K$ with $[r(c)] = \mu(c + \pi c')$;
3. for each $g \in G_K$, each $\varphi \in O_K[[X]]$ with $\varphi(0) = 0$, $\varphi'(0) = \chi(g)$ and $\varphi \circ f_\pi = f_\pi \circ \varphi$, and all $n$ and $D$, the element $v_n^D$ divides $g(v_n) - \sum_{i < D} r(\varphi_i)\, v_n^i$ in $\mathcal{O}^\flat$;
4. if $\mu = \mathrm{id}$, then $|v_n^\sharp - z_n| \leq |\pi|$ for all $n$.

Lean: `GlobalTheory.CompanionTheory.LTPer.Tilt.tilt_period`.

So the tilt condition of Definition 4.7.3 of Volume 4 is true.

*Proof.* We give the steps. First, estimates on the torsion system. From $z_{n+1}^q + \pi z_{n+1} = z_n$ and $z_1 \neq 0$ we get $|z_n| < 1$ for all $n$, a lower bound for $|z_n|$ when $n \geq 2$, and $|z_{n+1}^q - z_n| \leq |\pi|$.

Second, a Teichmüller approximation. A sequence in $\mathcal{O}_{\mathbb{C}_l}$ that is compatible under $x \mapsto x^q$ modulo $\pi$ comes from the tilt modulo $\pi$. So there are $u_n \in \mathcal{O}^\flat$ with $u_{n+1}^q = u_n$, $|u_n^\sharp - z_n| \leq |\pi|$ and $u_n \neq 0$. The lower bound on $|z_n|$ gives $u_n \neq 0$.

Third, the coefficients. Let $k$ be the residue field of $K$. It is perfect, so it embeds into $\mathcal{O}^\flat$, and the Teichmüller lift of the image of $\bar{c} \in k$ is the Teichmüller representative $\omega(c) \in O_K$ of $\bar{c}$. Let $r_0 : O_K \to \mathcal{O}^\flat$ be the reduction $O_K \to k$ followed by this embedding. Then $r_0$ is a ring map, $r_0(\pi) = 0$, and $[r_0(c)] = \omega(c) = c + \pi c'$ for some $c' \in O_K$.

Fourth, the twist by $\mu$. The embedding $\mu$ maps each root of unity $\zeta \in K$ of order prime to $l$ to $\zeta^{l^i}$ for one fixed $i \geq 0$, and we can take $i = 0$ if $\mu = \mathrm{id}$. Put $r = \mathrm{Frob}^i \circ r_0$, where $\mathrm{Frob}(x) = x^l$ on $\mathcal{O}^\flat$, and $v_n = u_n^{l^i}$. Then
$$\begin{aligned} [r(c)] &= [r_0(c)]^{l^i} = \omega(c)^{l^i} \\ &= \mu(\omega(c)) = \mu(c + \pi c'), \end{aligned}$$
which is condition 2. Condition 1 follows from $u_{n+1}^q = u_n$, $u_0 \neq 0$ and $|u_0^\sharp| = |u_0^\sharp - z_0| \leq |\pi| < 1$. Condition 4 holds since $i = 0$ and $v_n = u_n$ when $\mu = \mathrm{id}$.

Fifth, the Galois action. Since $\mathrm{Frob}^i$ is a ring map that commutes with $G_K$, condition 3 for $(r, v)$ follows from condition 3 for $(r_0, u)$. That case comes from $g(z_n) = \varphi(z_n)$ in the datum and from $|u_n^\sharp - z_n| \leq |\pi|$, by a compatibility of power series with Teichmüller sequences. We use this compatibility as a separate result and do not prove it here. $\square$

### The product condition

**Theorem 9.15.2 (Product condition).** Let $\chi : G_K \to K^\times$ be a homomorphism such that
$$N_{K/\mathbb{Q}_l}\bigl(\chi(g)\bigr) = \chi_{\mathrm{cyc}}(g) \quad \text{for each } g \in G_K \text{ that fixes } \mathbb{Q}_l^{\mathrm{ur}}.$$
For each embedding $\mu$ of $K$ let $t_\mu$ be a pre-period of $\chi$ at $\mu$. Then $t_{\mathrm{id}} \notin \mathrm{Fil}^2$, and $t_\mu \notin \mathrm{Fil}^1$ for $\mu \neq \mathrm{id}$.

Lean: `GlobalTheory.T.lubin_tate_period_not_filtered` (also `GlobalTheory.CompanionTheory.LTPer.exact_degrees_of_product`, the same statement).

So the product condition of Definition 4.7.6 of Volume 4 is true.

*Proof.* Let $L$ be the normal closure of $K$ in $\bar{\mathbb{Q}}_l$ and put $T = \prod_\mu t_\mu$. Each $t_\mu$ is nonzero and $B_{\mathrm{dR}}^+$ is a discrete valuation ring, so $T \neq 0$. Its maximal ideal is generated by Fontaine's element $t$. So $T = t^m u$ with $m \geq 0$ and $u$ a unit, and $m$ is the sum of the filtration degrees $d_\mu$ of the $t_\mu$.

For $\sigma \in G_L$ the pre-period property gives $\sigma(T) = \prod_\mu \mu(\chi(\sigma))\, T = N_{K/\mathbb{Q}_l}(\chi(\sigma))\, T$. By the hypothesis, $\sigma$ acts on $T$ through the cyclotomic character times an unramified character. Also $\sigma(t) = \chi_{\mathrm{cyc}}(\sigma)\, t$. So $u$ is a unit of $B_{\mathrm{dR}}^+$ on which $G_L$ acts through $\chi_{\mathrm{cyc}}^{1-m}$ times an unramified character. The image $\theta(u) \in \mathbb{C}_l$ is nonzero and has the same action. By Tate's theorem with Sen's theorem on unramified characters, this is possible only for $1 - m = 0$. So $m = 1$.

Now $\theta(t_{\mathrm{id}}) = 0$, so $d_{\mathrm{id}} \geq 1$. The degrees are at least $0$ and add to $1$. So $d_{\mathrm{id}} = 1$ and $d_\mu = 0$ for $\mu \neq \mathrm{id}$. $\square$

### The theorem

**Theorem 9.15.3 (de Rham Hecke characters).** Let $E$ be a number field, $\Omega$ an algebraic closure of $E$, $l$ a prime, $P$ a period datum at $l$ with a tie, $\iota : \bar{\mathbb{Q}}_l \to \mathbb{C}$ a field isomorphism and $\mathrm{art}$ a global Artin map. Let $\chi$ be an algebraic Hecke character of type $n$, and let $\mu : G_E \to \bar{\mathbb{Q}}_l^\times$ be a continuous homomorphism that is the $l$-adic character of $(\chi, n)$. Let $w$ be a finite place of $E$, $A$ a valuation ring of $\Omega$ above $w$, and take a local bridge at $A$ that induces $A$. Then:

1. the restriction of $\mu$ to the decomposition group $D_A$ is de Rham at $w$;
2. for each embedding $\tau : E \to \bar{\mathbb{Q}}_l$ that is induced by an embedding $\tau' : K_w \to L''$ into a finite extension $L''$ of $\mathbb{Q}_l$, the restriction of $\mu$ to $D_A$ has jumps $\{-n(\iota \circ \tau)\}$ at $\tau$.

Lean: `HodgeLocalDeRhamField.HLdR.field_outright` (also `UpperTheory.Lit.heckeLAdicCharacterDeRham`, a second name).

The terms are defined in Volume 4 ([Theorem 4.8.5 of Volume 4](/entry/field-of-lt-periods/)).

*Proof.* The tilt condition and the product condition hold by the two theorems above. Then the theorem on de Rham Hecke characters from these two conditions ([Theorem 4.8.6 of Volume 4](/entry/field-of-leaves/)) gives the result. That theorem writes $\mu$ near $w$ as a product of powers of Lubin-Tate characters ([Theorem 4.8.4 of Volume 4](/entry/lubin-tate-at-embedding/)), each with periods ([Theorem 4.7.7 of Volume 4](/entry/has-periods-main/)), times a character that is trivial on an open subgroup of inertia. $\square$

**Example 9.15.4.** Let $E = \mathbb{Q}$ and let $\chi = |\cdot|_{\mathbb{A}}$ be the norm character. For positive $k \in \mathbb{Q}^\times$ we have $\chi_\infty(k) = k$, so $\chi$ is algebraic of type $n = 1$. At $w = l$ the theorem says that the $l$-adic character $\mu$ is de Rham with the single jump $-1$. Here $\mu$ agrees on an open subgroup of inertia with the Lubin-Tate character of $\mathbb{Q}_l$ for $\pi = l$, which is the cyclotomic character $\chi_{\mathrm{cyc}}$. Its period is Fontaine's $t = \log[\varepsilon]$, which lies in $\mathrm{Fil}^1 \setminus \mathrm{Fil}^2$, and $t^{-1}$ spans $D_{\mathrm{dR}}(\chi_{\mathrm{cyc}})$, in filtration degree $-1$.

**Remark 9.15.5 (Formalization).** The theorem is `field_outright` in [Outright.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/HeckeLAdicCharacters/Outright.lean#L7). Its proof is the single term `field_of_leaves @tilt_period @lubin_tate_period_not_filtered` (L8). The module is in a folder named `PublishedTheorems`, but the theorem takes no hypotheses and uses no published result. The statement is `HeckeLAdicCharacterDeRham` in [HeckeLAdicCharacterDeRham.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/HeckeLAdicCharacterDeRham.lean#L11). We did not unfold `IsdRAt`, `IsJumpsAt`, `IsAlgPos`, `IsLAdicOf`, `IsGlobalArtin` or the map `rk1` that it applies to $\mu$; we read them through Volume 4. The statement asks for a tie of type `LocTied`, and the theorems below it use `LocTied6`, a structure with the same fields. The users are `UpperTheory.Gal.TP.Sub.charEx`, which uses it twice ([SubtractHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/SplitLineSubtraction/SubtractHolds.lean#L53)), and the second name in [HeckeDeRham.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GaloisRepresentations/HeckeDeRham.lean#L3). The tilt condition is `tilt_period` in [FrobPowRead.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FrobPowRead.lean#L139), a proof of about 226 lines. Its steps use `lubin_tate_sequence_norm_bounds`, `teichmuller_compatible_sequence_approximation`, `fix_ringHom`, `exp_twist` and `lubin_tate_teichmuller_sequence_compatibility`, which we did not open; the steps of the proof above are our reading of their names and of the way the proof uses them. The product condition is stated in [LubinTatePeriodNotFilteredStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LubinTatePeriodNotFilteredStatement.lean#L11). That file imports `Mathlib` twice (L1 and L3), raises `maxHeartbeats` to 1000000 for a proof of one line, and proves the statement with `first | exact @exact_degrees_of_product | ...`, with two fallbacks that are never needed. The real proof is `exact_degrees_of_product` in [LubinTatePeriodNotFiltered.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LubinTatePeriodNotFiltered.lean#L16), about 65 lines. It uses `maximalIdeal_eq_span_fontaineT`, `galois_action_period_product`, `hodge_tate_character_weight`, `sen_period_finite_extension`, `sen_unramified_character_period` and `period_product_filtration_levels`; we read their use but not their proofs.

## Notes and references

The chapter proves results that the main proof would otherwise take from the literature. The vanishing theorems of sections 1 to 6 and the Casselman-Wallach theorem of sections 7 and 8 reach the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/). Tate's global Euler characteristic formula of sections 9 to 12 reaches the step [EveryCharacter from Row0b](/step/every-character-of-row/). The Jacquet-Shalika bound of section 13, the Rankin-Selberg pole of section 14 and the de Rham property of this section reach the step [EveryCharacter](/step/every-character/), and the de Rham property also reaches the literature step through its second name.

Sections 1 to 3 follow Deligne and Illusie. Their decomposition theorem is stated for a smooth variety over a perfect field of dimension less than $p$ that lifts to $W_2$; here the proof uses an explicit atlas of Frobenius lifts. Sections 4 to 6 give the Kawamata-Viehweg theorem in characteristic $0$ by reduction modulo $p$, and then Nadel vanishing and local vanishing for multiplier ideals on a log resolution. The classical forms are stated for a nef and big $\mathbb{Q}$-divisor; here the boundary is an effective Cartier divisor with simple normal crossings, and the multiplier ideal is the pushforward from one log resolution.

Sections 7 and 8 prove the Casselman-Wallach theorem for the groups $U(p, q)$ only, with a maximum principle for $K$-finite vectors in the place of the classical analytic estimates. The classical theorem holds for all real reductive groups and says that the functor of smooth vectors of moderate growth is an equivalence from Harish-Chandra modules to its image.

Sections 9 to 12 prove Tate's formula $\prod_i \# H^i(G_S, M)^{(-1)^i} = \prod_{v \mid \infty} \# H^0(G_v, M) / |\# M|_v$ for a finite module $M$ whose order is a unit outside $S$. The proof reduces to modules killed by $l$, and then by restriction and induction to a coprime case. The reduction uses the theorem on induced characters in the form of Serre. The coprime case uses the Kummer sequence, the unit theorem and a count of $H^2$ from Poitou-Tate duality. Section 12 states the Poitou-Tate theorems in full, with the local invariant maps normalised at a uniformizer, and reduces them to fields in $\bar{\mathbb{Q}}$. Classically the local invariants are those of local class field theory, and the theorems hold for any finite module whose order is a unit outside $S$.

Section 13 gives the bound of Jacquet and Shalika: the Satake parameters $\alpha$ of a cuspidal representation of $\mathrm{GL}_a$ with unitary central character satisfy $N(w)^{-1/2} < |\alpha| < N(w)^{1/2}$. The statement here is for a totally complex field, and the proof uses the formula of Shintani. Section 14 gives the pole of the partial Rankin-Selberg $L$-function at $s = 1$; the classical form says that $L^S(s, \pi \times \tilde\pi')$ has a simple pole at $s = 1$ if $\pi \cong \pi'$ and is holomorphic there otherwise, while the statement here gives only the upper bound on the order of the pole. We know no source for the mirabolic step at the infinite places in the form given there.

Classically, the $l$-adic character of an algebraic Hecke character is locally algebraic above $l$, so it is de Rham there with jumps given by the infinity type. In the classical form the place lies above $l$; here any finite place with a local bridge is allowed, and only such places carry a bridge. The product condition uses the theorem of Tate on the cohomology of $\mathbb{C}_l(\chi)$.

- P. Deligne and L. Illusie, *Relèvements modulo $p^2$ et décomposition du complexe de de Rham*, Invent. Math. 89 (1987), 247-270.
- H. Esnault and E. Viehweg, *Lectures on Vanishing Theorems*, DMV Seminar 20, Birkhäuser, 1992.
- Y. Kawamata, *A generalization of Kodaira-Ramanujam's vanishing theorem*, Math. Ann. 261 (1982), 43-46.
- E. Viehweg, *Vanishing theorems*, J. reine angew. Math. 335 (1982), 1-8.
- R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics 52, Springer, 1977, Theorem III.12.8.
- A. M. Nadel, *Multiplier ideal sheaves and Kähler-Einstein metrics of positive scalar curvature*, Ann. of Math. 132 (1990), 549-596.
- R. Lazarsfeld, *Positivity in Algebraic Geometry I and II*, Ergeb. Math. Grenzgeb. (3) 48 and 49, Springer, 2004, Lemma 4.3.10 and Theorems 9.4.1 and 9.4.8.
- N. R. Wallach, *Real Reductive Groups II*, Pure and Applied Mathematics 132-II, Academic Press, 1992, Chapter 11.
- W. Casselman, *Canonical extensions of Harish-Chandra modules to representations of G*, Canad. J. Math. 41 (1989), 385-438.
- J. Bernstein and B. Krötz, *Smooth Fréchet globalizations of Harish-Chandra modules*, Israel J. Math. 199 (2014), 45-111.
- J. Tate, *Duality theorems in Galois cohomology over number fields*, Proc. Internat. Congr. Mathematicians (Stockholm, 1962), 288-295.
- J. S. Milne, *Arithmetic Duality Theorems*, Chapter I, Theorems 4.10 and 5.1.
- J. Neukirch, A. Schmidt and K. Wingberg, *Cohomology of Number Fields*, Theorems 8.6.10 and 8.7.4.
- J.-P. Serre, *Linear Representations of Finite Groups*, Graduate Texts in Mathematics 42, Springer, 1977, §9.2, Theorem 17.
- H. Jacquet and J. A. Shalika, *On Euler products and the classification of automorphic representations I*, Amer. J. Math. 103 (1981), 499-558, Corollary 2.5; *II*, Amer. J. Math. 103 (1981), 777-815, Theorem 4.4.
- T. Shintani, *On an explicit formula for class-1 "Whittaker functions" on $GL_n$ over $\mathfrak{P}$-adic fields*, Proc. Japan Acad. 52 (1976), 180-182.
- C. Moeglin and J.-L. Waldspurger, *Le spectre résiduel de $GL(n)$*, Ann. Sci. École Norm. Sup. (4) 22 (1989), 605-674, Appendice.
- J. Lubin and J. Tate, *Formal complex multiplication in local fields*, Ann. of Math. 81 (1965), 380-387.
- J.-M. Fontaine, *Le corps des périodes p-adiques*, Astérisque 223 (1994), Exposé II.
- J. Tate, *p-divisible groups*, in: Proceedings of a Conference on Local Fields (Driebergen, 1966), Springer, 1967, §3.
- J.-P. Serre, *Abelian l-adic Representations and Elliptic Curves*, Benjamin, 1968, Chapters II and III.
