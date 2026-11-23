---
title: The local Langlands correspondence from its inputs
decls:
  - GlobalTheory.LocLanglands.FieldCompat.fieldCompatible
  - GlobalTheory.T.local_langlands_transport
  - GlobalTheory.LocLanglandsBridge.localLanglandsGL_of_depthZero_zelevinsky_bernstein
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local Langlands correspondence from its inputs

The local Langlands correspondence for $\mathrm{GL}_n$ over a $p$-adic field is a bijection between irreducible smooth representations and Weil-Deligne representations ([the local Langlands correspondence](/learn/galois-representations/#the-local-langlands-correspondence)). It is characterized by Rankin-Selberg epsilon factors of pairs ([generic representations and local factors](/learn/representations/#generic-representations-and-local-factors)). This section proves the full statement used in this book from thirteen named inputs: the existence of a correspondence with a short list of properties, the local converse theorem, the Bernstein-Zelevinsky classification, results on depth zero, and global class field theory. The new content is a transport argument: the correspondence does not depend on how the local field is presented. [The theorem on ordinary adjoint cocycles](/entry/ord-van2/) uses the result.

Throughout, $E$ is a number field, $\Omega$ an algebraic closure of $E$, and $A \subseteq \Omega$ a valuation ring that lies over a finite place $w$ of $E$. Write $k = E_w$. The choice of $A$ fixes a decomposition group, and so a Weil group $W_k$ inside $\mathrm{Gal}(\Omega/E)$ ([the Weil group](/learn/galois-representations/#the-weil-group)). Let $\mathrm{Irr}(k)$ be the set of isomorphism classes of irreducible smooth representations of all the groups $\mathrm{GL}_n(k)$, $n \ge 0$, and let $\mathrm{WD}(k)$ be the set of isomorphism classes of finite-dimensional [Weil-Deligne representations](/learn/galois-representations/#weil-deligne-representations) of $W_k$. A *local Artin map* is a homomorphism $a \colon W_k \to k^\times$ that satisfies the laws of [local class field theory](/learn/class-field-theory/#local-class-field-theory). An *epsilon family* assigns to each nontrivial additive character $\psi$ of $k$ and each $y \in \mathrm{WD}(k)$ a number $\varepsilon(y, \psi) \in \mathbb{C}^\times$; it is *Deligne's* if it satisfies the laws of Deligne's local constants.

**Definition 8.8.1 (Laws of a reciprocity map).** Let $a$ be a local Artin map and $\varepsilon$ an epsilon family. A map $\mathrm{rec} \colon \mathrm{Irr}(k) \to \mathrm{WD}(k)$ satisfies the *minimal laws* for $(a, \varepsilon)$ if:

1. $\mathrm{rec}$ is a bijection, and $\mathrm{rec}(\pi)$ has dimension $n$ for $\pi$ a representation of $\mathrm{GL}_n(k)$;
2. for a smooth character $\chi$ of $k^\times = \mathrm{GL}_1(k)$, $\mathrm{rec}(\chi) = \chi \circ a$;
3. for $\pi$ cuspidal on $\mathrm{GL}_{m+1}(k)$, $\tau$ irreducible on $\mathrm{GL}_m(k)$ and $\psi$ nontrivial, the epsilon factor of the pair $(\pi, \tau)$ is $\varepsilon(\mathrm{rec}(\pi) \otimes \mathrm{rec}(\tau), \psi)$;
4. $\pi$ is cuspidal exactly when $\mathrm{rec}(\pi)$ is irreducible;
5. if $\pi$ is the Langlands quotient attached to segments $\Delta_1, \dots, \Delta_r$, where $\Delta_i$ has first term $\rho_i$ and length $l_i$, then $\mathrm{rec}(\pi) = \bigoplus_i \mathrm{rec}(\rho_i)|\cdot|^{(l_i - 1)/2} \otimes \mathrm{Sp}(l_i)$ ([cuspidal representations and segments](/learn/representations/#cuspidal-representations-and-segments)).

The *literal laws* add three more: $\mathrm{rec}$ commutes with twists by characters, the determinant of $\mathrm{rec}(\pi)$ is the central character of $\pi$ composed with $a$, and $\mathrm{rec}$ commutes with contragredients. The *full laws* add six more: the rules for characters composed with the determinant, for parabolic induction, and for supercuspidal supports; spherical representations correspond to unramified ones; the Satake parameter $\alpha$ gives $\mathrm{rec}(\pi) = \mathrm{diag}(\alpha_i^{-1})$; and $\pi$ has depth zero exactly when $\mathrm{rec}(\pi)$ is tame. We say that $\mathrm{rec}$ is a *literal* or a *full reciprocity map* if it satisfies the literal or the full laws for some local Artin map and some Deligne epsilon family.

**Definition 8.8.2 (Field compatibility).** Let $(E, \Omega, A, w)$ and $(E', \Omega', A', w')$ be two such data. A *place isomorphism* consists of a field isomorphism $\varphi \colon \Omega \to \Omega'$, a field embedding $j \colon E \to E'$ and a continuous ring isomorphism $i \colon E_w \to E'_{w'}$, such that $\varphi$ maps $A$ onto $A'$, $\varphi$ extends $j$, and $i$ extends $j$. Then $i$ carries representations of $\mathrm{GL}_n(E_w)$ to representations of $\mathrm{GL}_n(E'_{w'})$, and $\varphi$ relates Weil elements: $\sigma$ and $\sigma'$ correspond if $\varphi \circ \sigma = \sigma' \circ \varphi$. Two maps $\mathrm{rec}$ and $\mathrm{rec}'$ are *field compatible* if, for every place isomorphism and every pair $\pi, \pi'$ that correspond under $i$, there are matrix forms $b$ of $\mathrm{rec}(\pi)$ and $b'$ of $\mathrm{rec}'(\pi')$ with the same monodromy and $b(\sigma) = b'(\sigma')$ whenever $\sigma$ and $\sigma'$ correspond.

The statement *LocalLanglandsGL* says: for each $(E, \Omega, A, w)$ there is exactly one full reciprocity map, and any two full reciprocity maps are field compatible. The statement *LocalLanglandsExists* says only that a literal reciprocity map exists for each $(E, \Omega, A, w)$.

The other inputs are statements from the literature, in the following list.

- *Local converse*: two cuspidal representations of $\mathrm{GL}_{m+1}(k)$ with the same epsilon factors of pairs with all irreducible representations of $\mathrm{GL}_m(k)$ are isomorphic (Henniart).
- *Langlands exhaustion*, *Langlands multisegments*, *Zelevinsky polynomial ring*, *standard cosocle*, *geometric lemma* and *Bernstein-Zelevinsky finiteness*: the Bernstein-Zelevinsky and Zelevinsky theory of induced representations of $\mathrm{GL}_n(k)$.
- *Depth-zero cuspidal* and *depth-zero induction*: depth zero matches tameness for cuspidals, and depth zero passes to subquotients of induced representations.
- *Global Artin reciprocity*, *Chevalley units* and *Brauer in degree zero*: global class field theory, Chevalley's theorem that units congruent to $1$ modulo a suitable integer are $m$-th powers, and Brauer induction for virtual characters of degree zero.

**Theorem 8.8.3 (Transport of reciprocity maps).** Assume global Artin reciprocity, Chevalley units, Brauer in degree zero, LocalLanglandsExists, the local converse theorem, Langlands exhaustion and Bernstein-Zelevinsky finiteness. Let $\mathrm{rec}$ and $\mathrm{rec}'$ be literal reciprocity maps for $(E, \Omega, A, w)$ and $(E', \Omega', A', w')$. Then $\mathrm{rec}$ and $\mathrm{rec}'$ are field compatible.

Lean: `GlobalTheory.LocLanglands.FieldCompat.fieldCompatible` (also `GlobalTheory.T.local_langlands_transport`, a wrapper).

*Proof.* Fix a place isomorphism $(\varphi, j, i)$, and let $(a, \varepsilon)$ and $(a', \varepsilon')$ be the data of $\mathrm{rec}$ and $\mathrm{rec}'$. We take the following facts from the transport lemmas.

1. The inverse of $i$ is continuous, and $i$ preserves the valuation and the absolute value.
2. Transport by $i$ gives a bijection $T \colon \mathrm{Irr}(E_w) \to \mathrm{Irr}(E'_{w'})$ that keeps the degree, keeps cuspidality, keeps twists by $|\det|^s$, and maps a character $\chi$ to $\chi \circ i^{-1}$.
3. Transport by $\varphi$ gives a bijection $S \colon \mathrm{WD}(E_w) \to \mathrm{WD}(E'_{w'})$ that keeps the dimension, sums, tensor products, twists, the special representations $\mathrm{Sp}(l)$, irreducibility and characters.
4. Global Artin reciprocity and Chevalley's theorem give $a'(\sigma') = i(a(\sigma))$ when $\sigma$ and $\sigma'$ correspond.
5. Transport keeps epsilon factors of pairs: if $\psi' \circ i = \psi$, then pairs that correspond have the same epsilon factor.

Now put $\mathrm{rec}^\ast = S^{-1} \circ \mathrm{rec}' \circ T$, a map from $\mathrm{Irr}(E_w)$ to $\mathrm{WD}(E_w)$. Facts 2 to 5 show that $\mathrm{rec}^\ast$ satisfies the minimal laws for $a$ and for the epsilon family $(\psi, y) \mapsto \varepsilon'(S(y), \psi \circ i^{-1})$. For law 5 we transport the segments one at a time and use that $S$ commutes with sums, twists and $\mathrm{Sp}(l)$.

Choose a continuous nontrivial $\psi$ of $E_w$. Two Deligne epsilon families that are matched by a place isomorphism agree; this uses global Artin reciprocity, Chevalley's theorem, Brauer in degree zero and LocalLanglandsExists. So $\varepsilon(y, \psi) = \varepsilon'(S(y), \psi \circ i^{-1})$ for all $y$. Thus $\mathrm{rec}$ and $\mathrm{rec}^\ast$ satisfy the minimal laws for the same $a$ and epsilon families that agree at $\psi$. By the uniqueness lemma, which uses the local converse theorem, Langlands exhaustion and Bernstein-Zelevinsky finiteness, $\mathrm{rec} = \mathrm{rec}^\ast$. Then $\mathrm{rec}'(\pi') = \mathrm{rec}'(T\pi) = S(\mathrm{rec}(\pi))$, which is the statement of field compatibility. $\square$

**Theorem 8.8.4 (Local Langlands for $\mathrm{GL}_n$ from its inputs).** The thirteen statements LocalLanglandsExists, local converse, depth-zero cuspidal, depth-zero induction, Brauer in degree zero, Chevalley units, global Artin reciprocity, Langlands exhaustion, Langlands multisegments, standard cosocle, Zelevinsky polynomial ring, geometric lemma and Bernstein-Zelevinsky finiteness imply LocalLanglandsGL.

Lean: `GlobalTheory.LocLanglandsBridge.localLanglandsGL_of_depthZero_zelevinsky_bernstein`.

*Proof.* A literal reciprocity map is full, by a lemma that uses depth-zero cuspidal, depth-zero induction and the six statements on induced representations. Existence: LocalLanglandsExists gives a literal map, and it is full. Uniqueness: let $\mathrm{rec}$ be this map and $\mathrm{rec}'$ any full one. Both are literal. Apply the transport theorem to them with the identity place isomorphism $(\mathrm{id}_\Omega, \mathrm{id}_E, \mathrm{id}_{E_w})$, and to $\pi' = \pi$. This gives matrix forms of $\mathrm{rec}(\pi)$ and $\mathrm{rec}'(\pi)$ with the same monodromy and the same values on $W_k$. So the two classes are equal, and $\mathrm{rec} = \mathrm{rec}'$. Compatibility: full maps are literal, so the transport theorem applies to them directly. $\square$

The proof does not construct the correspondence. The existence is an input; the uniqueness and the compatibility come from the transport theorem.

**Remark 8.8.5 (Formalization).** The laws are `LawsMin` and `LawsLit` in [Langlands.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/Langlands.lean#L20), and the full laws `Laws`, the predicates `IsRec` and `FieldCompatible`, and the statement `LocalLanglandsGL` are in [LocalLanglandsGL.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/LocalLanglandsGL.lean#L96). The transport theorem is at [line 84 of LocalLanglandsTransport.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLanglandsTransport.lean#L84). Its wrapper `local_langlands_transport` is a `...Statement` file with `set_option maxHeartbeats 1000000` at line 18. The final theorem is at [line 22 of LocalLanglandsOfHyp.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLanglandsOfHyp.lean#L22); the step from literal to full maps is `rec_of_rec_literal`, the uniqueness lemma is `rec_unique_of_laws`, and the agreement of epsilon families is `rec_transport_field_iso`. We have not unfolded those three proofs or the transport lemmas. The uniqueness in the final theorem is the transport theorem with all three maps the identity (lines 35 to 46), and the existence is the hypothesis LocalLanglandsExists, so the content of the result is in the inputs. The local converse hypothesis asks for equal epsilon factors with every irreducible $\tau$ of $\mathrm{GL}_m$, where $m + 1$ is the degree of the cuspidal representations, and not with the smaller groups too. The hypothesis on depth-zero cuspidals is a statement about every literal reciprocity map, not about a fixed one.
